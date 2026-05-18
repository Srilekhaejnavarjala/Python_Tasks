# ============================================================
# SQLite Database Connection
# ============================================================

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import SQLITE_URL

# SQLite Engine
engine = create_engine(
    SQLITE_URL,
    connect_args={"check_same_thread": False}
)

# Session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base Class
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()