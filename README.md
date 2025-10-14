# 🎧 Audio Quality Analyzer

A lightweight Python project that records, mixes, denoises, and evaluates short audio clips — inspired by Apple's AirPods feature-testing workflows.

---

## 🚀 Overview

This mini-project simulates a practical audio-testing pipeline:  
**record → add noise → denoise → analyze → visualize**

It demonstrates how engineers can evaluate audio-processing performance using automated metrics and waveform analysis.  
The project is simple, reproducible, and extendable — ideal for showcasing applied ML, CoreAudio, and data-pipeline skills.

---

## 🧠 Tech Stack

**Languages:** Python 3 (Swift optional)  
**Libraries:** librosa, sounddevice, noisereduce, numpy, matplotlib, pandas  
**Apple Frameworks (optional):** CoreAudio, AVFoundation, SwiftUI  
**Platform:** macOS  

---

## 🔧 Features

- 🎙 Record clean speech and background noise  
- 🔊 Mix and denoise using a spectral-gating filter  
- 📈 Compute key metrics — SNR, RMS, Peak amplitude  
- 📊 Save results automatically to CSV  
- 🖼 Visualize before and after waveforms  
- 💬 Optional SwiftUI interface for user feedback (👍 / 👎)  

---

## ⚙️ Quick Start

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<yourusername>/audio-quality-analyzer.git
cd audio-quality-analyzer
```

### 2️⃣ Set Up Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install numpy scipy librosa soundfile sounddevice matplotlib pandas noisereduce
```

### 3️⃣ Record Audio Samples
```bash
python src/record.py 6 data/speech_clean.wav
python src/record.py 6 data/bg_noise.wav
```

### 4️⃣ Run the Pipeline
```bash
./run.sh
```

---

## 🧪 Example Outputs

| File | Description |
|------|--------------|
| 🎧 `outputs/mixed.wav` | Original voice with background noise |
| 🔈 `outputs/denoised.wav` | Cleaned audio after denoising |
| 📊 `outputs/metrics.csv` | Numeric metrics (SNR, RMS, Peak) |
| 🖼 `outputs/wave_before.png` | Waveform before denoising |
| 🖼 `outputs/wave_after.png` | Waveform after denoising |

---

## 🖥 Screenshots

| Terminal Run | Before | After |
|:--:|:--:|:--:|
| ![Terminal Output](screenshots/terminal_run.png) | ![Before](screenshots/wave_before.png) | ![After](screenshots/wave_after.png) |

---

## 📊 Metrics Example

| Metric | Before | After | Improvement |
|:--|--:|--:|--:|
| Signal-to-Noise Ratio (dB) | 2.4 | 9.8 | +7.4 |
| RMS Amplitude | 0.32 | 0.28 | −12.5% |
| Peak Amplitude | 0.98 | 0.73 | −25% |

> ✅ Denoising improved SNR ≈ 3× and visibly reduced noise amplitude.

---

## 💡 Future Enhancements

- 🤖 Integrate a real ML-based noise-reduction model (Core ML / TensorFlow Lite)  
- 🪄 Add an automatic feedback dashboard GUI  
- 🍎 Package as a lightweight macOS app  

---

## 🧾 Resume Summary

**Audio Quality Analyzer | Python · CoreAudio · AVFoundation · Librosa**  
Built a lightweight pipeline to record, mix, denoise, and analyze audio clips. Computed SNR/RMS metrics, visualized waveform fidelity, and logged results to CSV for regression testing — mirroring AirPods feature-testing workflows.

---

## 👨‍💻 Author

**Shreyansh Patel**  
M.S. in Computer Science, Cleveland State University  
📍 Cleveland, OH  
🔗 [LinkedIn](https://linkedin.com/in/your-profile) · 💻 [GitHub](https://github.com/yourusername)

---

⭐ If you like this project, give it a star!
