from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def test_memory():
    return {"message": "Memory endpoint working"}
