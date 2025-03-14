import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import time

temp_audio = "temp_audio.wav"

def record_audio(duration=5, sample_rate=16000):
    audio = []
    start_time = time.time()

    def callback(indata, frames, time, status):
        audio.append(indata.copy())

    with sd.InputStream(samplerate=sample_rate, channels=1, callback=callback, dtype=np.int16):
        while time.time() - start_time < duration:
            time.sleep(0.1)

    if len(audio) > 0:
        audio = np.concatenate(audio)
        wav.write(temp_audio, sample_rate, audio)
        return temp_audio
    return None
