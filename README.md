# 🎧 Audio Quality Analyzer

> A lightweight **Python + Swift (optional)** tool that records, mixes, denoises, and evaluates short audio clips — inspired by **Apple's AirPods feature-testing workflows**.

---

## 🚀 Overview
This mini-project simulates how Apple's Headphones & Accessories team tests audio models.  
It records real voice and noise samples, applies a denoising filter, and computes key metrics such as **SNR**, **RMS**, and **Peak Amplitude** to measure improvement.

---

## 🧠 Tech Stack
| Category | Tools Used |
|-----------|-------------|
| Language | Python 3, Swift (optional) |
| Libraries | `librosa`, `sounddevice`, `noisereduce`, `numpy`, `matplotlib`, `pandas` |
| Apple Frameworks (optional) | CoreAudio · AVFoundation · SwiftUI |
| Platform | macOS (works natively) |

---

## 🧩 Features
- 🎙 Record clean speech and background noise  
- 🔊 Mix + Denoise using spectral gating  
- 📈 Compute SNR/RMS metrics automatically  
- 🧾 Save metrics to CSV for comparison  
- 📊 Plot before and after waveforms  
- 💬 *(Optional)* SwiftUI feedback UI (👍 / 👎)

---

## ⚙️ Quick Start

```bash
# clone the repo
git clone https://github.com/<yourusername>/audio-quality-analyzer.git
cd audio-quality-analyzer

# set up environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt   # or install libs manually

# record clips
python src/record.py 6 data/speech_clean.wav
python src/record.py 6 data/bg_noise.wav

# run everything
./run.sh

