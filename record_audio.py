import threading
import time
import queue
import os

import sounddevice as sd
import soundfile as sf

MAX_DURATION = 60 * 50 # We can record sessions for up to 50 minutes
SAMPLE_RATE = 16000
CHANNELS = 1
WAV_OUTPUT = "lecture.wav"

recording = True

audio_queue = queue.Queue()

def audio_callback(indata, frames, time, status):
    audio_queue.put(indata.copy())

def record_audio():
    global recording
    if os.path.exists(WAV_OUTPUT):
        print(f"{WAV_OUTPUT} already exists!")
        os.remove(WAV_OUTPUT)

    with sf.SoundFile(WAV_OUTPUT, mode="x", samplerate=SAMPLE_RATE, channels=CHANNELS, subtype="PCM_16") as file:
        with sd.InputStream(samplerate=SAMPLE_RATE, channels=CHANNELS, callback=audio_callback):
            print("Recording has started.")
            start_time = time.time()

            while recording and (time.time() - start_time < MAX_DURATION):
                file.write(audio_queue.get())

            print("Recording has stopped.")

def start_recording():
    global recording, recording_thread
    recording = True

    recording_thread = threading.Thread(target = record_audio)
    recording_thread.start()

def stop_recording():
    global recording
    recording = False
    recording_thread.join()
