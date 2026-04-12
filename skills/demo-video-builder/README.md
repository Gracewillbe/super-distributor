## Demo Video Builder

**Claude Code skill for Super Distributor**

Turn an animated HTML page into a production-ready MP4 demo video — the kind you post to X, LinkedIn, or embed on a landing page.

---

## What It Does

This skill takes an animated HTML file and produces a **1080p MP4** ready for social media.

**You provide:**
- An animated HTML file (self-contained, single file)
- Optional: background music (external file or Web Audio API source)
- Target duration and aspect ratio

**You get:**
- H.264 MP4 at 1080p (or whatever size you specify)
- Synchronized audio (if you provided any)
- `+faststart` flag for instant web playback
- File size around 3-5 MB for a 30-second clip

---

## How to Use

### In Claude Code

```
Use the demo-video-builder skill
```

The skill will guide you through:
1. Point to your HTML file
2. Pick an audio mode (silent / external file / Web Audio API)
3. Set duration and aspect ratio
4. Run the render script
5. Verify the output

### Direct CLI

```bash
# One-time setup
pip install playwright imageio-ffmpeg
playwright install chromium

# Silent demo
python3 render_video.py --html demo.html --duration 30

# With background music
python3 render_video.py --html demo.html --duration 30 \
  --audio-file ~/Music/track.mp3

# With Web Audio API soundtrack (perfect sync)
python3 render_video.py --html demo.html --duration 37 \
  --audio-js examples/soundtrack-upbeat-tech.js
```

---

## Why This Exists

Most indie makers ship a landing page and then get stuck at "how do I show this on social media?"

The usual answers all suck:
- **Screen recording**: looks amateur, requires manual timing, no control over quality
- **Professional video editor**: overkill, expensive, slow
- **GIF**: looks dated, no sound, giant files
- **"I'll figure it out later"**: you won't

This skill closes the gap. You go from "animated HTML exists" to "MP4 is ready to post" in about 90 seconds, with no system dependencies and no manual work.

It's part of Super Distributor's core belief: **distribution is a skill, and skills can be automated.**

---

## Files in This Skill

| File | Purpose |
|------|---------|
| `skill.md` | Full skill instructions (loaded by Claude Code) |
| `README.md` | This file — user-facing overview |
| `render_video.py` | Python script that does the actual work |
| `examples/soundtrack-upbeat-tech.js` | Reference Web Audio soundtrack (~37s, 115 BPM) |

---

## Requirements

- Python 3.8+
- `playwright` (`pip install playwright && playwright install chromium`)
- `imageio-ffmpeg` (`pip install imageio-ffmpeg`)

Everything else is bundled. No Homebrew, no system ffmpeg, no Node, no editor installation.

---

## Part of Super Distributor

The open-source growth toolkit for indie makers.

→ github.com/Gracewillbe/super-distributor
