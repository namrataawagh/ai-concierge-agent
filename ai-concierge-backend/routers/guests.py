from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from models.models import Guest

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/guests")
def get_guests(db: Session = Depends(get_db)):
    return db.query(Guest).all()

@router.post("/guests")
def add_guest(guest: dict, db: Session = Depends(get_db)):
    new_guest = Guest(
        name=guest.get("name"),
        email=guest.get("email"),
        preferences=guest.get("preferences", {})
    )
    db.add(new_guest)
    db.commit()
    db.refresh(new_guest)
    return {"message": "Guest added", "guest": new_guest}
