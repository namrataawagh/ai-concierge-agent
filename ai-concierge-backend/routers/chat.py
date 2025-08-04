from fastapi import APIRouter
from schemas.chat import ChatRequest
from agents.assistant_agent import get_ai_response

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):
    response = get_ai_response(request.message)
    return {"response": response}
