# ============================================================
# MySQL Routes
# ============================================================

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.mysql import get_db

from app.schemas.department_schema import (
    DepartmentCreate,
    DepartmentResponse
)

from app.services.mysql_service import (
    create_department,
    get_departments,
    get_department_by_id,
    delete_department,
    search_employee_by_name,
    get_high_salary_employees
)

from app.schemas.employee_schema import (
    EmployeeCreate,
    EmployeeUpdate, 
    EmployeeResponse
)

from app.services.mysql_service import (
    create_employee,
    get_employees,
    get_employee_by_id,
    update_employee,
    delete_employee
)

from app.schemas.attendance_schema import (
    AttendanceCreate,
    AttendanceResponse
)

from app.services.mysql_service import (
    create_attendance,
    get_attendance,
    get_attendance_by_employee,
    delete_attendance
)

from app.schemas.salary_schema import (
    SalaryCreate,
    SalaryResponse
)

from app.services.mysql_service import (
    create_salary,
    get_salaries,
    get_salary_by_employee,
    delete_salary
)

# Router
router = APIRouter(
    prefix="/mysql",
    tags=["MySQL APIs"]
)


# ============================================================
# Create Department
# ============================================================

@router.post(
    "/departments",
    response_model=DepartmentResponse
)
def add_department(
    department: DepartmentCreate,
    db: Session = Depends(get_db)
):

    return create_department(db, department)


# ============================================================
# Get All Departments
# ============================================================

@router.get(
    "/departments",
    response_model=list[DepartmentResponse]
)
def all_departments(
    db: Session = Depends(get_db)
):

    return get_departments(db)


# ============================================================
# Get Department By ID
# ============================================================

@router.get(
    "/departments/{department_id}",
    response_model=DepartmentResponse
)
def single_department(
    department_id: int,
    db: Session = Depends(get_db)
):

    department = get_department_by_id(
        db,
        department_id
    )

    if not department:

        raise HTTPException(
            status_code=404,
            detail="Department Not Found"
        )

    return department


# ============================================================
# Delete Department
# ============================================================

@router.delete("/departments/{department_id}")
def remove_department(
    department_id: int,
    db: Session = Depends(get_db)
):

    department = delete_department(
        db,
        department_id
    )

    if not department:

        raise HTTPException(
            status_code=404,
            detail="Department Not Found"
        )

    return {
        "message": "Department Deleted Successfully"
    }

# ============================================================
# Create Employee
# ============================================================

@router.post(
    "/employees",
    response_model=EmployeeResponse
)
def add_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):

    return create_employee(db, employee)


# ============================================================
# Get All Employees
# ============================================================

@router.get(
    "/employees",
    response_model=list[EmployeeResponse]
)
def all_employees(
    db: Session = Depends(get_db)
):

    return get_employees(db)


# ============================================================
# Get Employee By ID
# ============================================================

@router.get(
    "/employees/{employee_id}",
    response_model=EmployeeResponse
)
def single_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    employee = get_employee_by_id(
        db,
        employee_id
    )

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    return employee


# ============================================================
# Update Employee
# ============================================================

@router.put(
    "/employees/{employee_id}",
    response_model=EmployeeResponse
)
def modify_employee(
    employee_id: int,
    employee: EmployeeUpdate,
    db: Session = Depends(get_db)
):

    updated_employee = update_employee(
        db,
        employee_id,
        employee
    )

    if not updated_employee:

        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    return updated_employee


# ============================================================
# Delete Employee
# ============================================================

@router.delete("/employees/{employee_id}")
def remove_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    employee = delete_employee(
        db,
        employee_id
    )

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    return {
        "message": "Employee Deleted Successfully"
    }

# ============================================================
# Create Attendance
# ============================================================

@router.post(
    "/attendance",
    response_model=AttendanceResponse
)
def mark_attendance(
    attendance: AttendanceCreate,
    db: Session = Depends(get_db)
):

    return create_attendance(
        db,
        attendance
    )


# ============================================================
# Get All Attendance
# ============================================================

@router.get(
    "/attendance",
    response_model=list[AttendanceResponse]
)
def all_attendance(
    db: Session = Depends(get_db)
):

    return get_attendance(db)


# ============================================================
# Get Attendance By Employee ID
# ============================================================

@router.get(
    "/attendance/employee/{employee_id}",
    response_model=list[AttendanceResponse]
)
def employee_attendance(
    employee_id: int,
    db: Session = Depends(get_db)
):

    return get_attendance_by_employee(
        db,
        employee_id
    )


# ============================================================
# Delete Attendance
# ============================================================

@router.delete("/attendance/{attendance_id}")
def remove_attendance(
    attendance_id: int,
    db: Session = Depends(get_db)
):

    attendance = delete_attendance(
        db,
        attendance_id
    )

    if not attendance:

        raise HTTPException(
            status_code=404,
            detail="Attendance Record Not Found"
        )

    return {
        "message": "Attendance Deleted Successfully"
    }

# ============================================================
# Create Salary
# ============================================================

@router.post(
    "/salary",
    response_model=SalaryResponse
)
def add_salary(
    salary: SalaryCreate,
    db: Session = Depends(get_db)
):

    return create_salary(
        db,
        salary
    )


# ============================================================
# Get All Salaries
# ============================================================

@router.get(
    "/salary",
    response_model=list[SalaryResponse]
)
def all_salaries(
    db: Session = Depends(get_db)
):

    return get_salaries(db)


# ============================================================
# Get Salary By Employee ID
# ============================================================

@router.get(
    "/salary/employee/{employee_id}",
    response_model=list[SalaryResponse]
)
def employee_salary(
    employee_id: int,
    db: Session = Depends(get_db)
):

    return get_salary_by_employee(
        db,
        employee_id
    )


# ============================================================
# Delete Salary
# ============================================================

@router.delete("/salary/{salary_id}")
def remove_salary(
    salary_id: int,
    db: Session = Depends(get_db)
):

    salary = delete_salary(
        db,
        salary_id
    )

    if not salary:

        raise HTTPException(
            status_code=404,
            detail="Salary Record Not Found"
        )

    return {
        "message": "Salary Deleted Successfully"
    }

# ============================================================
# Search Employee By Name
# ============================================================

@router.get("/search-employee/{employee_name}")
def search_employee(
    employee_name: str,
    db: Session = Depends(get_db)
):

    employees = search_employee_by_name(
        db,
        employee_name
    )

    return employees


# ============================================================
# Get High Salary Employees
# ============================================================

@router.get("/high-salary-employees")
def high_salary_employees(
    minimum_salary: float = 50000,
    db: Session = Depends(get_db)
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