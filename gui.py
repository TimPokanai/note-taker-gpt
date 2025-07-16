import tkinter as tk
from tkinter import scrolledtext
from threading import Thread

class NoteTakerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Lecture Note Taker")

        self.textbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=25)


if __name__ == "__main__":
    root = tk.Tk()
    app = NoteTakerApp(root)
    root.mainloop()
