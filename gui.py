from threading import Thread

import tkinter as tk
from tkinter import scrolledtext
import sounddevice as sd
import numpy as np

from record_audio import start_recording, stop_recording, WAV_OUTPUT
from transcribe_audio import transcribe_chunks
from summarize import summarize_full_transcript

class NoteTakerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Lecture Note Taker")

        self.textbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=25)
        self.textbox.pack(padx=10, pady=10)

        self.start_button = tk.Button(root, text="Start Recording", command=self.start_recording)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop Recording", command=self.stop_and_process, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

    def start_recording(self):
        self.textbox.insert(tk.END, "Recording started...\n")
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        Thread(target=start_recording).start()
            
    def stop_and_process(self):
        self.textbox.insert(tk.END, "Recording stopped. Transcribing...\n")
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        stop_recording()
        Thread(target=self.transcribe).start()

    def transcribe(self):
        transcript = transcribe_chunks(WAV_OUTPUT)
        summary = summarize_full_transcript(transcript)
        def update_gui():
            self.textbox.insert(tk.END, "Transcription done...\n")
            self.textbox.insert(tk.END, "\========== TRANSCRIBED NOTES ==========\n\n")
            self.textbox.insert(tk.END, summary)
            self.textbox.insert(tk.END, "\nDone.\n")
        self.root.after(0, update_gui)

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteTakerApp(root)
    root.mainloop()
