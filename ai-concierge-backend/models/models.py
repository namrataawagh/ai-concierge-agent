# Define tables
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Guest(Base):
    __tablename__ = "guests"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    preferences = Column(JSON)

class Room(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    price = Column(Integer)
    available = Column(Boolean)

class Package(Base):
    __tablename__ = "packages"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    tags = Column(JSON)

class Request(Base):
    __tablename__ = "requests"
    id = Column(Integer, primary_key=True)
    guest_id = Column(Integer, ForeignKey("guests.id"))
    type = Column(String)
    status = Column(String)
