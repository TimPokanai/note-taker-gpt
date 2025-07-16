import whisper

model = whisper.load_model("base")

def transcribe_audio(filename="lecture.wav"):
    print("Starting audio transcription...")
    result = model.transcribe(filename, fp16=False)
    print("Audio transcription complete!")
    return result["text"]
