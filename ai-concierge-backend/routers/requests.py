from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import SessionLocal
from models.models import Request
from schemas.request import RequestCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/requests")
def create_request(request: RequestCreate, db: Session = Depends(get_db)):
    new_request = Request(
        guest_id=request.guest_id,
        type=request.type,
        status=request.status
    )
    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    return {"message": "Request created", "request": new_request}

@router.get("/requests")
def get_requests(db: Session = Depends(get_db)):
    return db.query(Request).all()
