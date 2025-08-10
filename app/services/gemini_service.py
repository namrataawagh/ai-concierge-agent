import google.generativeai as genai

# ✅ Replace this with your Gemini API key
genai.configure(api_key="AIzaSyDnszCJ6NC7pTSCNwBHKpMJTQK3qg_YbLoY")

def classify_intent(user_message: str) -> str:
    prompt = f"What is the intent of this message: '{user_message}'? Reply with a single keyword like 'booking', 'greeting', 'help', etc."

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return response.text.strip()
