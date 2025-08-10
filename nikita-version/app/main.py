from fastapi import FastAPI

from app.services.intent_classifier import classify_intent
from app.services.memory_store import get_memory
from app.database import create_db_and_tables, get_session
from app.models import ChatMessage
from app.routers import chat, intent, memory

app = FastAPI()

create_db_and_tables()

# Routers
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(intent.router, prefix="/intent", tags=["Intent"])
app.include_router(memory.router, prefix="/memory", tags=["Memory"])

@app.get("/")
def root():
    return {"message": "AI Concierge Backend 2 is running"}

@app.get("/history")
def history():
    return {"conversation": get_memory()}

@app.get("/history-db")
def get_chat_from_db():
    session = get_session()
    messages = session.query(ChatMessage).all()
    return messages
