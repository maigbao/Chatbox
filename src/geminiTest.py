from google import genai
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

gemini = OpenAI(api_key=GEMINI_API_KEY, base_url=GEMINI_BASE_URL)


respond = gemini.chat.completions.create(
    model="gemini-3.7-flash",   
    messages=[
        {"role": "user", "content": "Explain how AI works in a few words"}
    ]
)

print(respond.choices[0].message.content)