import whisper

def transcribe_audio(filename="lecture.wav"):
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    return result["text"]
