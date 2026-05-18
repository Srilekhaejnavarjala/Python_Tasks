# ============================================================
# SQLite Routes
# ============================================================

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.sqlite_db import get_sqlite_db

from app.models.sql_models import Base
from app.database.sqlite_db import engine

# Create SQLite Tables
Base.metadata.create_all(bind=engine)

# Schemas
from app.schemas.department_schema import (
    DepartmentCreate,
    DepartmentResponse
)

from app.schemas.employee_schema import (
    EmployeeCreate,
    EmployeeUpdate,
    EmployeeResponse
)

from app.schemas.attendance_schema import (
    AttendanceCreate,
    AttendanceResponse
)

from app.schemas.salary_schema import (
    SalaryCreate,
    SalaryResponse
)

# Services
from app.services.mysql_service import *

# Router
router = APIRouter(
    prefix="/sqlite",
    tags=["SQLite APIs"]
)


# ============================================================
# Department APIs
# ============================================================

@router.post(
    "/departments",
    response_model=DepartmentResponse
)
def add_department(
    department: DepartmentCreate,
    db: Session = Depends(get_sqlite_db)
):

    return create_department(db, department)


@router.get(
    "/departments",
    response_model=list[DepartmentResponse]
)
def all_departments(
    db: Session = Depends(get_sqlite_db)
):

    return get_departments(db)


# ============================================================
# Employee APIs
# ============================================================

@router.post(
    "/employees",
    response_model=EmployeeResponse
)
def add_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_sqlite_db)
):

    return create_employee(db, employee)


@router.get(
    "/employees",
    response_model=list[EmployeeResponse]
)
def all_employees(
    db: Session = Depends(get_sqlite_db)
):

    return get_employees(db)


# ============================================================
# Attendance APIs
# ============================================================

@router.post(
    "/attendance",
    response_model=AttendanceResponse
)
def add_attendance(
    attendance: AttendanceCreate,
    db: Session = Depends(get_sqlite_db)
):

    return create_attendance(db, attendance)


@router.get(
    "/attendance",
    response_model=list[AttendanceResponse]
)
def all_attendance(
    db: Session = Depends(get_sqlite_db)
):

    return get_attendance(db)


# ============================================================
# Salary APIs
# ============================================================

@router.post(
    "/salary",
    response_model=SalaryResponse
)
def add_salary(
    salary: SalaryCreate,
    db: Session = Depends(get_sqlite_db)
):

    return create_salary(db, salary)


@router.get(
    "/salary",
    response_model=list[SalaryResponse]
)
def all_salaries(
    db: Session = Depends(get_sqlite_db)
):

    return get_salaries(db)

# ============================================================
# Search Employee By Name
# ============================================================

@router.get("/search-employee/{employee_name}")
def search_employee(
    employee_name: str,
    db: Session = Depends(get_sqlite_db)
):

    return search_employee_by_name(
        db,
        employee_name
    )


# ============================================================
# Get High Salary Employees
# ============================================================

@router.get("/high-salary-employees")
def high_salary_employees(
    minimum_salary: float = 50000,
    db: Session = Depends(get_sqlite_db)
):

    salaries = get_high_salary_employees(
        db,
        minimum_salary
    )

    result = []

    for salary in salaries:

        result.append({

            "employee_id": salary.employee.id,
            "employee_name": salary.employee.name,
            "salary": salary.salary,
            "bonus": salary.bonus
        })

    return result