# ============================================================
# Main FastAPI Application
# ============================================================

from fastapi import FastAPI

# MySQL Engine
from app.database.mysql import engine

#Import MongoDB Client
from app.database import mongodb

# SQL Models
from app.models.sql_models import Base

# Import MySQL Router
from app.routers.mysql_routes import router as mysql_router
#Import MongoDB Router
from app.routers.mongo_routes import router as mongo_router

# Import SQLite Router
from app.routers.sqlite_routes import router as sqlite_router

# Create Tables
Base.metadata.create_all(bind=engine)

# FastAPI App
app = FastAPI(
    title="Employee Management System",
    description="FastAPI Multi Database Project",
    version="1.0.0"
)

# Include Routers
app.include_router(mysql_router)
#Including SQLite Router
app.include_router(sqlite_router)
#Including MongoDB Router
app.include_router(mongo_router)


# ============================================================
# Home Route
# ============================================================

@app.get("/")
def home():

    return {
        "message": "Employee Management System Running Successfully"
    }