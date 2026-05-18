# ============================================================
# MySQL Database Connection
# ============================================================

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import MYSQL_URL

# Create MySQL Engine
engine = create_engine(MYSQL_URL)

# Create Session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base Class
Base = declarative_base()

# Dependency Function
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()