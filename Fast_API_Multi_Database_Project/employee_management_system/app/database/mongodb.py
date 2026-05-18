# ============================================================
# MongoDB Atlas Connection
# ============================================================

from mongoengine import connect

from app.config import MONGO_URL

# Connect MongoDB Atlas
connect(host=MONGO_URL)