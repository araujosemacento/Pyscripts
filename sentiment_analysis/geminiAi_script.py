#-*- coding: utf-8 -*-

import os
import google.generativeai as genai

API_KEY = os.getenv("GLC_API_KEY")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

prompt=input("\n\nEscreva uma frase, para aferir o sentimento atrelado a ela:\n\n-> ")

response = (
    model.generate_content(f"O sentimento exposto no texto \"{prompt}\" é neutro, negativo ou positivo?")._result.candidates[0].content.parts[0].text.lower()
)

print(f"\n\033[4mSentimento {response}\n")
