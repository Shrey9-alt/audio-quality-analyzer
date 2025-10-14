import numpy as np, soundfile as sf, librosa, noisereduce as nr, pathlib

speech_p = pathlib.Path("data/speech_clean.wav")
noise_p  = pathlib.Path("data/bg_noise.wav")
mixed_p  = pathlib.Path("outputs/mixed.wav")
den_p    = pathlib.Path("outputs/denoised.wav")
mixed_p.parent.mkdir(parents=True, exist_ok=True)

speech, sr = librosa.load(speech_p, sr=None, mono=True)
noise, _   = librosa.load(noise_p,  sr=sr,   mono=True)

# match lengths
if len(noise) < len(speech):
    reps = int(np.ceil(len(speech)/len(noise)))
    noise = np.tile(noise, reps)[:len(speech)]
else:
    noise = noise[:len(speech)]

alpha = 0.35  # noise level (0.2–0.5 typical)
mixed = speech + alpha*noise
sf.write(mixed_p, mixed, sr)

# simple denoise (spectral gating)
denoised = nr.reduce_noise(y=mixed, sr=sr)
sf.write(den_p, denoised, sr)
print("Wrote:", mixed_p, "and", den_p)
