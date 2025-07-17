import math
import tempfile
import os

import whisper
import torchaudio

model = whisper.load_model("base")

def transcribe_chunks(file_path, chunk_length=30):
    waveform, sr = torchaudio.load(file_path)
    duration = waveform.size(1) / sr
    full_transcript = ""

    for i in range(0, math.ceil(duration / chunk_length)):
        start = i * chunk_length
        end = min((i + 1) * chunk_length, duration)

        chunk_waveform = waveform[:, int(start * sr):int(end * sr)]

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
            torchaudio.save(tmp_file.name, chunk_waveform, sr)
            result = model.transcribe(tmp_file.name, fp16=False)
            print(result["text"])
            full_transcript += result["text"] + " "
            os.remove(tmp_file.name)

    return full_transcript
