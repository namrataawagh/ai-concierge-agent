from fastapi import FastAPI
from db.database import init_db

app = FastAPI()

# Run DB init
init_db()

@app.get("/")
def read_root():
    return {"message": "AI Concierge Backend is live!"}
