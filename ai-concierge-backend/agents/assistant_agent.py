# agents/assistant_agent.py

from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
    google_api_key=os.getenv("GOOGLE_API_KEY")  # ✅ This should now work
)

def get_ai_response(message: str) -> str:
    response = llm.invoke(message)
    return response.content if hasattr(response, "content") else str(response)
