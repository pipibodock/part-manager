from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
SessionLocal = None
engine = None

def init_engine(database_url: str):
    global engine, SessionLocal
    engine = create_engine(database_url)
    SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    if SessionLocal is None:
        raise RuntimeError("Database engine not initialized. Call init_engine() first.")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
