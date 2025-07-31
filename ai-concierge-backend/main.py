from fastapi import FastAPI
from db.database import init_db, SessionLocal
from routers import guests
from models.models import Guest, Room

app = FastAPI()

# Initialize DB tables
init_db()

# ✅ Seed mock data for Day 1
def seed_data():
    db = SessionLocal()

    # Seed guests only if empty
    if not db.query(Guest).first():
        guest1 = Guest(
            name="Jack",
            email="jack@example.com",
            preferences={"food": "vegetarian", "likes": ["spa", "nature"]}
        )
        guest2 = Guest(
            name="Namrata",
            email="namrata@example.com",
            preferences={"food": "non-veg", "likes": ["adventure", "city tours"]}
        )
        db.add_all([guest1, guest2])

    # Seed rooms only if empty
    if not db.query(Room).first():
        room1 = Room(type="Deluxe", price=5500, available=True)
        room2 = Room(type="Suite", price=9500, available=False)
        db.add_all([room1, room2])

    db.commit()
    db.close()

seed_data()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "AI Concierge Backend is live!"}

# Add the /guests routes
app.include_router(guests.router)
