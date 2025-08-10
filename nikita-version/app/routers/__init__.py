from fastapi import APIRouter
from pydantic import BaseModel
from app.services.gemini_service import classify_intent

router = APIRouter()

class IntentRequest(BaseModel):
    message: str

@router.post("/")
def detect_intent(request: IntentRequest):
    intent = classify_intent(request.message)
    return {"intent": intent}
