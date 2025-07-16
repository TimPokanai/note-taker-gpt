import threading
import time
import queue
import os

import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write
from transcribe_audio import transcribe_audio

MAX_DURATION = 60 * 50 # We can record sessions for up to 50 minutes
SAMPLE_RATE = 16000
CHANNELS = 1
WAV_OUTPUT = "lecture.wav"

recording = True

audio_queue = queue.Queue()

# def record_audio(filename="lecture.wav", duration=30, fs=16000):
#     print("Recording...")

#     audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype="int16")
#     sd.wait()
#     write(filename, fs, audio)

#     print(f"Saved to {filename}")

def audio_callback(indata, frames, time, status):
    audio_queue.put(indata.copy())

def record_audio():

    if os.path.exists(WAV_OUTPUT):
        print(f"{WAV_OUTPUT} already exists!")
        os.remove(WAV_OUTPUT)

    with sf.SoundFile(WAV_OUTPUT, mode="x", samplerate=SAMPLE_RATE, channels=CHANNELS, subtype="PCM_16") as file:
        with sd.InputStream(samplerate=SAMPLE_RATE, channels=CHANNELS, callback=audio_callback):
            print("Recording has started. Press ENTER to stop early.")
            start_time = time.time()

            while recording and (time.time() - start_time < MAX_DURATION):
                file.write(audio_queue.get())

            print("Recording has stopped.")

def start_recording():
    global recording
    recording = True

    recording_thread = threading.Thread(target = record_audio)
    recording_thread.start()

    input("Press ENTER to stop recording\n")
    recording = False
    recording_thread.join()

def process():
    transcript = transcribe_audio(WAV_OUTPUT)
    print("Transcription complete.")
    print(transcript)

if __name__ == "__main__":
    start_recording()
    process()
