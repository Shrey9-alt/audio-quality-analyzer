# Audio Quality Analyzer

Lightweight tool to evaluate noise-reduction on short audio clips.

## What it does
- Records clean speech + background noise (or uses existing WAVs)
- Mixes them, denoises via spectral-gating
- Computes metrics (SNR, RMS, peak) and saves to CSV
- Plots before/after waveforms

## Why this matters (Apple San Diego role)
Mirrors AirPods feature-testing workflows: audio data collection, pipeline, metrics, and evaluation.

## Quickstart
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install numpy scipy librosa soundfile sounddevice matplotlib pandas noisereduce
python src/record.py 6 data/speech_clean.wav
python src/record.py 6 data/bg_noise.wav
./run.sh
