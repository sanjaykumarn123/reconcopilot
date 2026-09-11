from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

engine = create_engine("sqlite:///reconcopilot.db")
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)