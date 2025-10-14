🎧 Audio Quality Analyzer
=====================================
A lightweight Python + Swift (optional) tool that records, mixes, denoises, and evaluates short audio clips — inspired by Apple's AirPods audio feature-testing workflows.

-------------------------------------
🚀 Overview
-------------------------------------
This mini-project simulates a real-world audio-testing pipeline:
record → add noise → denoise → analyze → visualize.
It demonstrates how software engineers can evaluate audio-ML behavior through automated metrics and waveform visualization.

-------------------------------------
🧠 Tech Stack
-------------------------------------
Language: Python 3, Swift (optional)
Libraries: librosa, sounddevice, noisereduce, numpy, matplotlib, pandas
Apple Frameworks (optional): CoreAudio, AVFoundation, SwiftUI
Platform: macOS (native)

-------------------------------------
🧩 Features
-------------------------------------
🎙 Record clean speech and background noise
🔊 Mix + Denoise using spectral gating
📈 Compute SNR / RMS / Peak metrics
🧾 Save metrics to CSV for comparisons
🖼 Visualize before & after waveforms
💬 Optional SwiftUI interface for user feedback (👍 / 👎)

-------------------------------------
⚙️ Quick Start
-------------------------------------
# clone the repo
git clone https://github.com/<yourusername>/audio-quality-analyzer.git
cd audio-quality-analyzer

# create & activate environment
python3 -m venv .venv
source .venv/bin/activate
pip install numpy scipy librosa soundfile sounddevice matplotlib pandas noisereduce

# record clips
python src/record.py 6 data/speech_clean.wav
python src/record.py 6 data/bg_noise.wav

# run everything
./run.sh

-------------------------------------
🧪 Example Outputs
-------------------------------------
🎧 outputs/mixed.wav          → Original voice + background noise
🔈 outputs/denoised.wav       → Cleaned audio after filter
📊 outputs/metrics.csv        → Numeric metrics (SNR, RMS, Peak)
🖼 outputs/wave_before.png    → Waveform before denoising
🖼 outputs/wave_after.png     → Waveform after denoising

-------------------------------------
📸 Screenshots
-------------------------------------
Terminal Run: screenshots/terminal_run.png
Waveforms Before: screenshots/wave_before.png
Waveforms After:  screenshots/wave_after.png

-------------------------------------
📊 Metrics Example
-------------------------------------
Metric                    | Before | After | Improvement
---------------------------|---------|--------|-------------
Signal-to-Noise Ratio (dB) | 2.4     | 9.8    | +7.4
RMS Amplitude              | 0.32    | 0.28   | -12.5%
Peak Amplitude             | 0.98    | 0.73   | -25%

Denoising improved SNR ≈ 3× and visibly reduced noise amplitude.

-------------------------------------
💡 Future Improvements
-------------------------------------
- Integrate real ML noise-reduction model (Core ML / TensorFlow Lite)
- Add auto-GUI feedback dashboard
- Deploy as a small macOS app

-------------------------------------
🧾 Resume Summary
-------------------------------------
Audio Quality Analyzer | Python · CoreAudio · AVFoundation · Librosa
Built a lightweight pipeline to record, mix, denoise, and analyze audio clips; computed SNR/RMS metrics and visualized waveform fidelity; logged results to CSV for regression testing — mirrors AirPods feature-testing workflows.

-------------------------------------
👨‍💻 Author
-------------------------------------
Shreyansh Patel
M.S. Computer Science @ Cleveland State University
📍 Cleveland, OH
💼 LinkedIn: https://linkedin.com/in/your-profile
💻 GitHub:   https://github.com/yourusername

⭐ If you like this project, give it a star!
