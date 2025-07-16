import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(transcript):
    prompt = (
        "You are a university note-taker AI. Convert the following lecture transcript into well-formatted, "
        "concise bullet point notes with topic headers, key concepts, and definitions where applicable.\n\n"
        f"Transcript:\n{transcript}"
    )
