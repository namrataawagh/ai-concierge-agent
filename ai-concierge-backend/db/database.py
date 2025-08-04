from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base

DATABASE_URL = "postgresql://concierge_user:123456@localhost/concierge"

engine = create_engine(DATABASE_URL)  # ✅ No 'connect_args'
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
