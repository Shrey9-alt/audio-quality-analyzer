#!/usr/bin/env bash
set -e
source .venv/bin/activate
python src/mix_and_denoise.py
python src/metrics.py
python src/plot.py
open outputs/wave_before.png
open outputs/wave_after.png
