import numpy as np
import time
from vosk import Model, KaldiRecognizer
import pyaudio

# Initialize model and recognizer
model = Model(r"C:\Users\73220\PycharmProjects\vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

# Initialize PyAudio
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

# Define silence detection parameters
silence_threshold = 500  # Volume level threshold to consider as silence
silence_duration = 30  # Duration in seconds to wait before stopping on silence
start_silence = None

try:
    while True:
        data = stream.read(4096)

        # Calculate volume level
        audio_data = np.frombuffer(data, dtype=np.int16)
        volume_level = np.sqrt(np.mean(audio_data ** 2))

        # Check if the volume level is below the threshold
        if volume_level < silence_threshold:
            if start_silence is None:
                start_silence = time.time()
            elif time.time() - start_silence >= silence_duration:
                print("Silence detected. Stopping the stream...")
                break
        else:
            start_silence = None  # Reset the silence timer if volume is above threshold

        # Process the audio data with the recognizer
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            print(text[14:-3])

finally:
    stream.stop_stream()
    stream.close()
    mic.terminate()
    print("Stream stopped.")
