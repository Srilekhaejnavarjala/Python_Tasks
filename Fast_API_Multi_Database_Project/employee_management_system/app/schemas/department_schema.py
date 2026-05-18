# ============================================================
# Department Schemas
# ============================================================

from pydantic import BaseModel


# Create Department Schema
class DepartmentCreate(BaseModel):

    name: str
    location: str


# Response Schema
class DepartmentResponse(DepartmentCreate):

    id: int

    class Config:
        from_attributes = True