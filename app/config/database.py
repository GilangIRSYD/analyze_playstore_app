import os
from contextlib import contextmanager

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


load_dotenv(override=True)

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Session DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@contextmanager
def get_db_contex():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()