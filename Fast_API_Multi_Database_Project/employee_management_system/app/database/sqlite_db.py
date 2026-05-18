# ============================================================
# SQLite Database Configuration
# ============================================================

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


# SQLite Database URL
DATABASE_URL = "sqlite:///./employee_sqlite.db"


# Create Engine
engine = create_engine(
    DATABASE_URL,
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


# ============================================================
# Dependency
# ============================================================

def get_sqlite_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()