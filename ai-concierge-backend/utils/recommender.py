# Basic rule-based recommender
from sqlalchemy.orm import Session
from models.models import Guest, Room

def recommend_room(db: Session, guest_name: str) -> str:
    guest = db.query(Guest).filter(Guest.name == guest_name).first()

    if not guest:
        return f"Guest '{guest_name}' not found."

    preferences = guest.preferences
    preferred_keywords = preferences.get("likes", [])
    food_pref = preferences.get("food", "any")

    # Get all available rooms
    rooms = db.query(Room).filter(Room.available == True).all()

    if not rooms:
        return "No rooms available at the moment."

    # Simple matching logic
    for room in rooms:
        if room.type.lower() == "suite" and "luxury" in preferred_keywords:
            return f"We recommend the Suite for {guest_name} – it's perfect for luxury lovers."
        elif room.type.lower() == "deluxe" and "spa" in preferred_keywords:
            return f"We recommend the Deluxe room for {guest_name} – great for spa lovers."

    return f"We recommend the {rooms[0].type} room for {guest_name}."
