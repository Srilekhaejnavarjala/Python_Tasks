# ============================================================
# Employee Schemas
# ============================================================

from pydantic import BaseModel
from typing import Optional


# Create Employee Schema
class EmployeeCreate(BaseModel):

    name: str
    age: int
    email: str
    phone: str
    designation: str
    department_id: int


# Update Schema
class EmployeeUpdate(BaseModel):

    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    designation: Optional[str] = None
    department_id: Optional[int] = None


# Response Schema
class EmployeeResponse(EmployeeCreate):

    id: int

    class Config:
        from_attributes = True

# ============================================================
# Mongo Employee Schema
# ============================================================

class MongoEmployeeCreate(BaseModel):

    name: str
    age: int
    email: str
    phone: str
    designation: str
    department_id: str
