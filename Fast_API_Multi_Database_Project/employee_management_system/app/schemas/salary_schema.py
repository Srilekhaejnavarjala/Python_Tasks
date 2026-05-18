# ============================================================
# Salary Schemas
# ============================================================

from pydantic import BaseModel


class SalaryCreate(BaseModel):

    employee_id: int
    salary: float
    bonus: float


class SalaryResponse(SalaryCreate):

    id: int

    class Config:
        from_attributes = True

# ============================================================
# Mongo Salary Schema
# ============================================================

class MongoSalaryCreate(BaseModel):

    employee_id: str
    salary: float
    bonus: float