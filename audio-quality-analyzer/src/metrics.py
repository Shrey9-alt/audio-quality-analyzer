import numpy as np, pandas as pd, soundfile as sf, pathlib, time

def rms(x): return float(np.sqrt(np.mean(np.square(x))))
def peak(x): return float(np.max(np.abs(x)))

def snr(ref, test):
    # higher is better; compares test to reference (ref ≈ clean)
    num = np.mean(ref**2)
    den = np.mean((ref - test)**2) + 1e-12
    return float(10*np.log10(num/den))

base = pathlib.Path("outputs"); base.mkdir(exist_ok=True)
speech, sr = sf.read("data/speech_clean.wav")
mixed,  _  = sf.read("outputs/mixed.wav")
den,    _  = sf.read("outputs/denoised.wav")

row = {
  "snr_mixed_vs_clean": snr(speech, mixed),
  "snr_denoised_vs_clean": snr(speech, den),
  "rms_clean": rms(speech),
  "rms_mixed": rms(mixed),
  "rms_denoised": rms(den),
  "peak_clean": peak(speech),
  "peak_mixed": peak(mixed),
  "peak_denoised": peak(den),
  "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
}

csv = base/"metrics.csv"
df = pd.DataFrame([row])
if csv.exists():
    old = pd.read_csv(csv)
    df = pd.concat([old, df], ignore_index=True)

df.to_csv(csv, index=False)
print("Metrics:\n", df.tail(1).to_string(index=False))
print("Saved →", csv)
