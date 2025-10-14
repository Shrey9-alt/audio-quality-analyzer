import matplotlib.pyplot as plt, soundfile as sf, numpy as np, pathlib

out = pathlib.Path("outputs"); out.mkdir(exist_ok=True)

def plot_wav(wav_path, png_path, title):
    x, sr = sf.read(wav_path)
    t = np.arange(len(x))/sr
    plt.figure()
    plt.plot(t, x)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(png_path, dpi=160)
    plt.close()

plot_wav("outputs/mixed.wav",   "outputs/wave_before.png", "Waveform: Mixed (Noisy)")
plot_wav("outputs/denoised.wav","outputs/wave_after.png",  "Waveform: Denoised")
print("Saved plots:", "outputs/wave_before.png", "outputs/wave_after.png")
