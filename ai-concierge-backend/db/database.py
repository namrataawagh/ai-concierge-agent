# DB connection
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base

DATABASE_URL = "sqlite:///./concierge.db"  # Use PostgreSQL URL if needed

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
