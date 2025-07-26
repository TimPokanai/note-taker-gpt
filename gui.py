import tkinter as tk
from tkinter import scrolledtext
from threading import Thread

from record_audio import record_audio
from transcribe_audio import transcribe_chunks

class NoteTakerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Lecture Note Taker")

        self.textbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=25)
        self.textbox.pack(padx=10, pady=10)

        self.start_button = tk.Button(root, text="Start Recording", command=self.start_recording)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop Recording", state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        self.recording = False
        self.audio_frames = []
        self.fs = 16000

    def start_recording(self):
            Thread(target=self.process).start()

    def process(self):
            record_audio("lecture.wav", duration=300)
            transcript = transcribe_chunks("lecture.wav")
            self.textbox.insert(tk.END, transcript)

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteTakerApp(root)
    root.mainloop()
