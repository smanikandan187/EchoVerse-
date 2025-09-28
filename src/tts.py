import numpy as np
import soundfile as sf
from transformers import pipeline

# Parler-TTS open-source model
tts_pipe = pipeline("text-to-speech", model="parler-tts/parler-tts-mini-v1", device_map="auto")

def synthesize(text, download_path='output.wav'):
    tts_output = tts_pipe(text)
    # tts_output contains .audio and .sampling_rate
    audio_array = np.array(tts_output["audio"])
    sampling_rate = tts_output["sampling_rate"]
    # Save as WAV file
    sf.write(download_path, audio_array, sampling_rate)
    return download_path
