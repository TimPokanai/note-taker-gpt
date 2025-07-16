import threading

import sounddevice as sd
from scipy.io.wavfile import write

MAX_DURATION = 60 * 50 # We can record sessions for up to 50 minutes
SAMPLE_RATE = 16000
CHANNELS = 1
WAV_OUTPUT = "lecture.wav"

recording = True

def record_audio(filename="lecture.wav", duration=30, fs=16000):
    print("Recording...")

    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype="int16")
    sd.wait()
    write(filename, fs, audio)

    print(f"Saved to {filename}")

def start_recording():
    global recording
    recording = True

    recording_thread = threading.Thread(target = record_audio)
    recording_thread.start()

    input("Press ENTER to stop recording\n")
    recording = False
    recording_thread.join()
