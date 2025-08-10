from fastapi import APIRouter
from pydantic import BaseModel

from app.services.gemini_service import classify_intent
from app.services.memory_store import save_to_memory
from app.models import ChatMessage
from app.database import get_session

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/send")
def send_message(chat_request: ChatRequest):
    user_message = chat_request.message
    session = get_session()

    # Save to in-memory store
    save_to_memory("user", user_message)

    # Save user message to DB
    user_entry = ChatMessage(sender="user", message=user_message)
    session.add(user_entry)
    session.commit()

    # Generate bot response
    bot_response = classify_intent(user_message)

    # Save bot message to in-memory store
    save_to_memory("bot", bot_response)

    # Save bot message to DB
    bot_entry = ChatMessage(sender="bot", message=bot_response)
    session.add(bot_entry)
    session.commit()

    return {"response": bot_response}