# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

# SQLite DB placed at project root
DATABASE_URL = "sqlite:///./chat_history.db"

# For SQLite, need the connect arg below
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# factory for Session objects
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def create_db_and_tables():
    """Call this once at startup to create the DB file and tables if missing."""
    Base.metadata.create_all(bind=engine)

def get_session():
    """Return a new SQLAlchemy Session object."""
    return SessionLocal()