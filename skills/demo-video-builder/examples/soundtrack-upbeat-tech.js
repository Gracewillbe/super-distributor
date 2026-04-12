// Upbeat tech-demo soundtrack (~37 seconds)
// -------------------------------------------
// Drop this file into render_video.py via: --audio-js examples/soundtrack-upbeat-tech.js
//
// Variables provided by render_video.py:
//   offlineCtx   — an OfflineAudioContext you should schedule sound on
//   DURATION     — duration in seconds
//   SAMPLE_RATE  — sample rate (typically 44100)
//
// This track is C major: C - Am - F - G, 115 BPM, 72 beats (~37s).
// Use it as-is or tweak the patterns below to match your own demo.

const t = 0;
const BPM = 115;
const beat = 60 / BPM;
const totalBeats = 72;

// Master envelope: ramp in (0-1.5s), hold, fade out (33-37s)
const master = offlineCtx.createGain();
master.gain.setValueAtTime(0, t);
master.gain.linearRampToValueAtTime(0.18, t + 1.5);
master.gain.setValueAtTime(0.18, t + 33);
master.gain.linearRampToValueAtTime(0, t + 37);
master.connect(offlineCtx.destination);

// ---- Synth primitives ----
function noise(time, dur, vol) {
  const bufSize = Math.max(1, Math.floor(offlineCtx.sampleRate * dur));
  const buf = offlineCtx.createBuffer(1, bufSize, offlineCtx.sampleRate);
  const data = buf.getChannelData(0);
  for (let i = 0; i < bufSize; i++) data[i] = Math.random() * 2 - 1;
  const src = offlineCtx.createBufferSource();
  src.buffer = buf;
  const hp = offlineCtx.createBiquadFilter();
  hp.type = 'highpass';
  hp.frequency.value = 7000;
  const g = offlineCtx.createGain();
  g.gain.setValueAtTime(vol, time);
  g.gain.exponentialRampToValueAtTime(0.001, time + dur);
  src.connect(hp); hp.connect(g); g.connect(master);
  src.start(time);
  src.stop(time + dur);
}

function kick(time, vol = 0.35) {
  const osc = offlineCtx.createOscillator();
  const g = offlineCtx.createGain();
  osc.type = 'sine';
  osc.frequency.setValueAtTime(150, time);
  osc.frequency.exponentialRampToValueAtTime(40, time + 0.12);
  g.gain.setValueAtTime(vol, time);
  g.gain.exponentialRampToValueAtTime(0.001, time + 0.3);
  osc.connect(g); g.connect(master);
  osc.start(time); osc.stop(time + 0.35);
}

function snap(time, vol = 0.12) {
  const osc = offlineCtx.createOscillator();
  const g = offlineCtx.createGain();
  osc.type = 'triangle';
  osc.frequency.value = 1200;
  g.gain.setValueAtTime(vol, time);
  g.gain.exponentialRampToValueAtTime(0.001, time + 0.06);
  osc.connect(g); g.connect(master);
  osc.start(time); osc.stop(time + 0.08);
  noise(time, 0.04, vol * 0.6);
}

function hihat(time, vol = 0.06) {
  noise(time, 0.03, vol);
}

function bass(time, freq, dur, vol = 0.15) {
  const osc = offlineCtx.createOscillator();
  const g = offlineCtx.createGain();
  osc.type = 'sine';
  osc.frequency.value = freq;
  g.gain.setValueAtTime(vol, time);
  g.gain.setValueAtTime(vol, time + dur - 0.05);
  g.gain.linearRampToValueAtTime(0, time + dur);
  osc.connect(g); g.connect(master);
  osc.start(time); osc.stop(time + dur + 0.01);
}

function pluck(time, freq, vol = 0.07) {
  const osc = offlineCtx.createOscillator();
  const g = offlineCtx.createGain();
  osc.type = 'triangle';
  osc.frequency.value = freq;
  g.gain.setValueAtTime(vol, time);
  g.gain.exponentialRampToValueAtTime(0.001, time + 0.25);
  osc.connect(g); g.connect(master);
  osc.start(time); osc.stop(time + 0.3);
}

// ---- Chord progression: C - Am - F - G ----
const chords = [
  { bass: 65.41, notes: [261.63, 329.63, 392.00] },  // C
  { bass: 55.00, notes: [261.63, 329.63, 440.00] },  // Am
  { bass: 43.65, notes: [261.63, 349.23, 440.00] },  // F
  { bass: 49.00, notes: [293.66, 392.00, 493.88] },  // G
];

// ---- Main pattern ----
for (let b = 0; b < totalBeats; b++) {
  const bt = t + b * beat;
  const chordIdx = Math.floor(b / 8) % 4;  // change chord every 2 bars
  const ch = chords[chordIdx];
  const barPos = b % 4;

  // Kick on 1 & 3
  if (barPos === 0 || barPos === 2) kick(bt, 0.3);
  // Snap on 2 & 4
  if (barPos === 1 || barPos === 3) snap(bt, 0.1);
  // 8th-note hi-hat
  hihat(bt, 0.045);
  hihat(bt + beat / 2, 0.03);
  // Bass root on beat 1 of each bar
  if (barPos === 0) bass(bt, ch.bass, beat * 3.5, 0.13);

  // Pluck arpeggio — starts after 2 beats intro
  if (b >= 4) {
    if (barPos === 0 || barPos === 2) pluck(bt, ch.notes[0], 0.05);
    if (barPos === 1) pluck(bt, ch.notes[1], 0.05);
    if (barPos === 3) {
      pluck(bt, ch.notes[2], 0.04);
      pluck(bt + beat / 2, ch.notes[0] * 2, 0.03);  // octave sparkle
    }
  }

  // Extra high sparkle every 8 beats
  if (b >= 8 && b % 8 === 0) {
    pluck(bt, ch.notes[2] * 2, 0.04);
  }
}
