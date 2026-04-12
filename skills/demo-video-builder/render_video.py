#!/usr/bin/env python3
"""
demo-video-builder: Turn an animated HTML file into a production-ready MP4.

Part of Super Distributor (github.com/Gracewillbe/super-distributor).

Usage:
  python3 render_video.py --html path/to/demo.html [options]

Examples:
  # Silent 30s video at 1080p
  python3 render_video.py --html demo.html --duration 30

  # With external audio file (mp3/wav/m4a)
  python3 render_video.py --html demo.html --audio-file music.mp3 --duration 30

  # With Web Audio API soundtrack (offline-rendered for perfect sync)
  python3 render_video.py --html demo.html --audio-js soundtrack.js --duration 37

Dependencies:
  pip install playwright imageio-ffmpeg
  playwright install chromium
"""

from __future__ import annotations

import argparse
import asyncio
import base64
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional

try:
    from playwright.async_api import async_playwright
except ImportError:
    sys.exit(
        "Missing dependency: playwright\n"
        "  pip install playwright && playwright install chromium"
    )

try:
    import imageio_ffmpeg
except ImportError:
    sys.exit(
        "Missing dependency: imageio-ffmpeg\n"
        "  pip install imageio-ffmpeg"
    )

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()


# ---- WAV encoder injected into the page ----
WAV_ENCODER_JS = r"""
function __encodeWav(buffer) {
  const numChannels = buffer.numberOfChannels;
  const length = buffer.length;
  const sampleRate = buffer.sampleRate;
  const byteLength = 44 + length * numChannels * 2;
  const arrayBuffer = new ArrayBuffer(byteLength);
  const view = new DataView(arrayBuffer);
  let off = 0;
  const writeStr = (s) => {
    for (let i = 0; i < s.length; i++) view.setUint8(off++, s.charCodeAt(i));
  };
  writeStr('RIFF');
  view.setUint32(off, byteLength - 8, true); off += 4;
  writeStr('WAVE');
  writeStr('fmt ');
  view.setUint32(off, 16, true); off += 4;
  view.setUint16(off, 1, true); off += 2;            // PCM
  view.setUint16(off, numChannels, true); off += 2;
  view.setUint32(off, sampleRate, true); off += 4;
  view.setUint32(off, sampleRate * numChannels * 2, true); off += 4;
  view.setUint16(off, numChannels * 2, true); off += 2;
  view.setUint16(off, 16, true); off += 2;
  writeStr('data');
  view.setUint32(off, length * numChannels * 2, true); off += 4;
  const chans = [];
  for (let i = 0; i < numChannels; i++) chans.push(buffer.getChannelData(i));
  for (let i = 0; i < length; i++) {
    for (let c = 0; c < numChannels; c++) {
      let s = chans[c][i];
      if (s > 1) s = 1; else if (s < -1) s = -1;
      view.setInt16(off, s < 0 ? s * 0x8000 : s * 0x7FFF, true);
      off += 2;
    }
  }
  const bytes = new Uint8Array(arrayBuffer);
  let binary = '';
  const chunkSize = 0x8000;
  for (let i = 0; i < bytes.length; i += chunkSize) {
    binary += String.fromCharCode.apply(null, bytes.subarray(i, i + chunkSize));
  }
  return btoa(binary);
}
"""


async def render_audio_offline(p, user_js: str, duration: int, sample_rate: int) -> bytes:
    """Run user-provided Web Audio scheduling code in a headless OfflineAudioContext.

    The user JS runs with these variables in scope:
      - offlineCtx: an OfflineAudioContext(2, sampleRate * duration, sampleRate)
      - DURATION  : duration in seconds (integer)
      - SAMPLE_RATE: sample rate

    It should schedule all sound on `offlineCtx` and connect everything to
    `offlineCtx.destination`. No need to call startRendering() — this script does.
    """
    full_js = f"""
    async () => {{
      const DURATION = {duration};
      const SAMPLE_RATE = {sample_rate};
      const offlineCtx = new OfflineAudioContext(2, SAMPLE_RATE * DURATION, SAMPLE_RATE);

      // ===== User schedule code begins =====
      {user_js}
      // ===== User schedule code ends =====

      const rendered = await offlineCtx.startRendering();
      {WAV_ENCODER_JS}
      return __encodeWav(rendered);
    }}
    """
    browser = await p.chromium.launch()
    try:
        page = await browser.new_page()
        await page.goto("about:blank")
        b64 = await page.evaluate(full_js)
        return base64.b64decode(b64)
    finally:
        await browser.close()


async def record_video(
    p,
    html_path: Path,
    duration_ms: int,
    width: int,
    height: int,
    do_click: bool,
    wait_before_ms: int,
    video_dir: Path,
) -> Path:
    video_dir.mkdir(parents=True, exist_ok=True)
    for f in video_dir.iterdir():
        f.unlink()
    browser = await p.chromium.launch()
    try:
        context = await browser.new_context(
            viewport={"width": width, "height": height},
            device_scale_factor=1,
            record_video_dir=str(video_dir),
            record_video_size={"width": width, "height": height},
        )
        page = await context.new_page()
        await page.goto(html_path.as_uri())
        await page.wait_for_timeout(wait_before_ms)
        if do_click:
            # Click center — triggers pages that wait for a user gesture
            # (required on most browsers before AudioContext / autoplay works)
            await page.mouse.click(width // 2, height // 2)
        await page.wait_for_timeout(duration_ms)
        video_handle = page.video
        await context.close()
        return Path(await video_handle.path())
    finally:
        await browser.close()


def merge(
    video_path: Path,
    audio_path: Optional[Path],
    output: Path,
    duration: int,
) -> None:
    if output.exists():
        output.unlink()
    cmd = [
        FFMPEG,
        "-y",
        "-hide_banner",
        "-loglevel", "error",
        "-i", str(video_path),
    ]
    if audio_path is not None:
        cmd += ["-i", str(audio_path), "-map", "0:v:0", "-map", "1:a:0"]
    else:
        cmd += ["-map", "0:v:0"]
    cmd += [
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-preset", "medium",
        "-crf", "18",
    ]
    if audio_path is not None:
        cmd += ["-c:a", "aac", "-b:a", "192k"]
    cmd += [
        "-movflags", "+faststart",
        "-t", str(duration),
        str(output),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("ffmpeg failed:", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        raise SystemExit(1)


async def run(args) -> None:
    html_path = Path(args.html).resolve()
    if not html_path.exists():
        sys.exit(f"HTML file not found: {html_path}")

    output = Path(args.output).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    tmp_dir = output.parent / "_demo_render_tmp"
    tmp_dir.mkdir(parents=True, exist_ok=True)
    audio_wav = tmp_dir / "audio.wav"
    video_dir = tmp_dir / "videos"

    external_audio: Optional[Path] = None

    async with async_playwright() as p:
        # ---- Step 1: audio ----
        if args.audio_js:
            js_path = Path(args.audio_js).resolve()
            if not js_path.exists():
                sys.exit(f"audio-js file not found: {js_path}")
            user_js = js_path.read_text(encoding="utf-8")
            print(f"[1/3] Rendering audio offline from {js_path.name} ...")
            wav_bytes = await render_audio_offline(
                p, user_js, args.duration, args.audio_sample_rate
            )
            audio_wav.write_bytes(wav_bytes)
            external_audio = audio_wav
            print(f"       -> {audio_wav.name} ({len(wav_bytes):,} bytes)")
        elif args.audio_file:
            src = Path(args.audio_file).resolve()
            if not src.exists():
                sys.exit(f"audio-file not found: {src}")
            external_audio = src
            print(f"[1/3] Using external audio: {src.name}")
        else:
            print("[1/3] No audio — producing silent video")

        # ---- Step 2: record visuals ----
        print(f"[2/3] Recording {args.width}x{args.height} video for {args.duration}s ...")
        video_path = await record_video(
            p,
            html_path,
            duration_ms=args.duration * 1000,
            width=args.width,
            height=args.height,
            do_click=not args.no_click,
            wait_before_ms=int(args.wait_before_record * 1000),
            video_dir=video_dir,
        )
        print(f"       -> {video_path.name}")

    # ---- Step 3: encode MP4 ----
    print("[3/3] Encoding H.264 MP4 ...")
    merge(video_path, external_audio, output, args.duration)
    size_mb = output.stat().st_size / (1024 * 1024)
    print(f"\n✅ {output} ({size_mb:.1f} MB)")

    if not args.keep_tmp:
        shutil.rmtree(tmp_dir, ignore_errors=True)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Turn an animated HTML file into a 1080p MP4 demo video.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--html", required=True, help="Path to the animated HTML file")
    parser.add_argument("--output", default="demo-video.mp4", help="Output MP4 path (default: demo-video.mp4)")
    parser.add_argument("--duration", type=int, default=30, help="Recording duration in seconds (default: 30)")
    parser.add_argument("--width", type=int, default=1920, help="Video width (default: 1920)")
    parser.add_argument("--height", type=int, default=1080, help="Video height (default: 1080)")
    audio_group = parser.add_mutually_exclusive_group()
    audio_group.add_argument("--audio-file", help="External audio file to merge (mp3/wav/m4a)")
    audio_group.add_argument(
        "--audio-js",
        help="JS file with OfflineAudioContext scheduling code (for Web Audio soundtracks)",
    )
    parser.add_argument("--audio-sample-rate", type=int, default=44100, help="Audio sample rate (default: 44100)")
    parser.add_argument(
        "--no-click",
        action="store_true",
        help="Don't auto-click the page center (use if your animation auto-plays)",
    )
    parser.add_argument(
        "--wait-before-record",
        type=float,
        default=0.3,
        help="Seconds to wait after page load before clicking (default: 0.3)",
    )
    parser.add_argument("--keep-tmp", action="store_true", help="Keep intermediate files for debugging")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    asyncio.run(run(args))


if __name__ == "__main__":
    main()
