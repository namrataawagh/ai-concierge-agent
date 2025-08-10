# app/models.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the declarative base for SQLAlchemy models
Base = declarative_base()

class ChatMessage(Base):
    __tablename__ = "chatmessage"  # Name of the table in SQLite

    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String, nullable=False)    # "user" or "bot"
    message = Column(String, nullable=False)   # Text content
