from fastapi import APIRouter
from pydantic import BaseModel
from app.services.gemini_service import classify_intent

router = APIRouter()

class IntentRequest(BaseModel):
    message: str

@router.post("/")
def get_intent(request: IntentRequest):
    user_message = request.message
    intent = classify_intent(user_message)
    return {"intent": intent}
