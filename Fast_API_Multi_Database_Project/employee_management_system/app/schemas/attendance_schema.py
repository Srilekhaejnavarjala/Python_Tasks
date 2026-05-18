# ============================================================
# Attendance Schemas
# ============================================================

from pydantic import BaseModel
from datetime import date


class AttendanceCreate(BaseModel):

    employee_id: int
    date: date
    status: str


class AttendanceResponse(AttendanceCreate):

    id: int

    class Config:
        from_attributes = True

# ============================================================
# Mongo Attendance Schema
# ============================================================

class MongoAttendanceCreate(BaseModel):

    employee_id: str
    date: date
    status: str