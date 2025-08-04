# agents/assistant_agent.py

from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from utils.recommender import recommend_room
from db.database import SessionLocal
import os

load_dotenv()

llm = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
    google_api_key=os.getenv("GOOGLE_API_KEY")  # ✅ This should now work
)

def get_ai_response(message: str) -> str:
    db = SessionLocal()

    try:
        if "recommend" in message.lower():
            # For now, hardcoded guest name. Later, we can extract dynamically
            return recommend_room(db, "Namrata")

        # If not recommendation, fallback to Gemini
        ai_response = llm.invoke(message)
        return ai_response.content

    finally:
        db.close()
