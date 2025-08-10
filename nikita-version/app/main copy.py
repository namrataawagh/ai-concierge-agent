from app.gemini_service import classify_intent




from fastapi import FastAPI
from app.memory_service import get_memory

from database import create_db_and_tables, get_session  # ✅ NEW
from models import ChatMessage  # ✅ NEW

from app.routers import chat, intent, memory

app = FastAPI()

create_db_and_tables()  # ✅ Create the DB file and table

# Include routers
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(intent.router, prefix="/intent", tags=["Intent"])
app.include_router(memory.router, prefix="/memory", tags=["Memory"])

@app.get("/")
def root():
    return {"message": "AI Concierge Backend 2 is running"}

@app.get("/history")
def history():
    return {"conversation": get_memory()}

@app.get("/history-db")  # ✅ New: fetch from database
def get_chat_from_db():
    session = get_session()
    messages = session.query(ChatMessage).all()
    return messages
