import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("ERROR: No se encontró la clave API. Asegúrate de que el archivo .env está configurado correctamente.")

client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

def generate_history(prompt):
    answer = client.chat.completions.create(
        model="perplexity/r1-1776",
        messages=[{"role": "system", "content": "Eres un creador de historias."},
                  {"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=200
    )
    return answer.choices[0].message.content

prompt = "Genera una historia corta sobre un pirata en una isla misteriosa."
history = generate_history(prompt)
print(history)