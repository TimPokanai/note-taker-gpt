from dotenv import load_dotenv

from openai import OpenAI

load_dotenv()
client = OpenAI()

MODEL = "gpt-3.5-turbo-16k"

def summarize_full_transcript(transcript):
    if not transcript.strip():
        return "Transcript is empty. Nothing to summarize"

    system_prompt = "You are an expert university lecture summarizer. Create a detailed, structured summary from the following lecture transcript. Organize the notes into bullet points by topic."
    user_prompt = f"Transcript:\n\n{transcript}"

    try:
        response = client.chat.completions.create(
            model = MODEL,
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature = 0.3,
            max_tokens=2000
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"OpenAI API error: {e}"
