import sounddevice as sd, soundfile as sf, sys, pathlib

sr = 16000
dur = float(sys.argv[1]) if len(sys.argv) > 1 else 6.0
out = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else pathlib.Path("data/out.wav")
out.parent.mkdir(parents=True, exist_ok=True)

print(f"Recording {dur}s → {out} at {sr} Hz…")
audio = sd.rec(int(dur*sr), samplerate=sr, channels=1, dtype="float32")
sd.wait()
sf.write(str(out), audio.squeeze(), sr)
print("Saved:", out)
