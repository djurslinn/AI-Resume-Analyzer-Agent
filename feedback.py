import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_feedback(sections):
    feedback = {}
    for sec, text in sections.items():
        if not text:
            feedback[sec] = "No content found. Please add this section."
            continue
        prompt = f"Rewrite this resume section to be clear, concise, impactful, and professional:\n{text}\n"
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                max_tokens=150,
                temperature=0.7
            )
            feedback[sec] = response.choices[0].text.strip()
        except Exception as e:
            feedback[sec] = f"Error generating feedback: {e}"
    return feedback
