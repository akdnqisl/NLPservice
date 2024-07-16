import google.generativeai as genai

with open("API_KEY.txt", "r") as f:
    API_KEY = f.read().strip()

genai.configure(api_key=API_KEY)
