# ============================================================
# MongoDB Routes
# ============================================================

from fastapi import APIRouter
from fastapi import HTTPException

from app.schemas.department_schema import (
    DepartmentCreate
)

from app.services.mongo_service import (
    create_department,
    get_departments,
    get_department_by_id,
    delete_department
)

from app.schemas.employee_schema import (
    MongoEmployeeCreate
)

from app.services.mongo_service import (
    create_employee,
    get_employees,
    get_employee_by_id,
    delete_employee,
    search_employee_by_name,
    get_high_salary_employees
)

from app.schemas.attendance_schema import (
    MongoAttendanceCreate
)

from app.services.mongo_service import (
    create_attendance,
    get_attendance,
    get_attendance_by_employee,
    delete_attendance
)

from app.schemas.salary_schema import (
    MongoSalaryCreate
)

from app.services.mongo_service import (
    create_salary,
    get_salaries,
    get_salary_by_employee,
    delete_salary
)

# Router
router = APIRouter(
    prefix="/mongo",
    tags=["MongoDB APIs"]
)


# ============================================================
# Create Department
# ============================================================

@router.post("/departments")
def add_department(department: DepartmentCreate):

    new_department = create_department(
        department
    )

    return {
        "id": str(new_department.id),
        "name": new_department.name,
        "location": new_department.location
    }


# ============================================================
# Get All Departments
# ============================================================

@router.get("/departments")
def all_departments():

    departments = get_departments()

    result = []

    for dept in departments:

        result.append({

            "id": str(dept.id),
            "name": dept.name,
            "location": dept.location
        })

    return result


# ============================================================
# Get Department By ID
# ============================================================

@router.get("/departments/{department_id}")
def single_department(department_id: str):

    department = get_department_by_id(
        department_id
    )

    if not department:

        raise HTTPException(
            status_code=404,
            detail="Department Not Found"
        )

    return {

        "id": str(department.id),
        "name": department.name,
        "location": department.location
    }


# ============================================================
# Delete Department
# ============================================================

@router.delete("/departments/{department_id}")
def remove_department(department_id: str):

    department = delete_department(
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

@router.post("/employees")
def add_employee(employee: MongoEmployeeCreate):

    new_employee = create_employee(
        employee
    )

    if not new_employee:

        raise HTTPException(
            status_code=404,
            detail="Department Not Found"
        )

    return {

        "id": str(new_employee.id),
        "name": new_employee.name,
        "age": new_employee.age,
        "email": new_employee.email,
        "phone": new_employee.phone,
        "designation": new_employee.designation,
        "department": str(new_employee.department.id)
    }


# ============================================================
# Get All Employees
# ============================================================

@router.get("/employees")
def all_employees():

    employees = get_employees()

    result = []

    for emp in employees:

        result.append({

            "id": str(emp.id),
            "name": emp.name,
            "age": emp.age,
            "email": emp.email,
            "phone": emp.phone,
            "designation": emp.designation,
            "department": str(emp.department.id)
        })

    return result


# ============================================================
# Get Employee By ID
# ============================================================

@router.get("/employees/{employee_id}")
def single_employee(employee_id: str):

    employee = get_employee_by_id(
        employee_id
    )

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    return {

        "id": str(employee.id),
        "name": employee.name,
        "age": employee.age,
        "email": employee.email,
        "phone": employee.phone,
        "designation": employee.designation,
        "department": str(employee.department.id)
    }


# ============================================================
# Delete Employee
# ============================================================

@router.delete("/employees/{employee_id}")
def remove_employee(employee_id: str):

    employee = delete_employee(
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

@router.post("/attendance")
def add_attendance(
    attendance: MongoAttendanceCreate
):

    new_attendance = create_attendance(
        attendance
    )

    if not new_attendance:

        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    return {

        "id": str(new_attendance.id),
        "employee": str(new_attendance.employee.id),
        "date": new_attendance.date,
        "status": new_attendance.status
    }


# ============================================================
# Get All Attendance
# ============================================================

@router.get("/attendance")
def all_attendance():

    attendance_records = get_attendance()

    result = []

    for attendance in attendance_records:

        result.append({

            "id": str(attendance.id),
            "employee": str(attendance.employee.id),
            "date": attendance.date,
            "status": attendance.status
        })

    return result


# ============================================================
# Get Attendance By Employee
# ============================================================

@router.get("/attendance/employee/{employee_id}")
def employee_attendance(employee_id: str):

    attendance_records = get_attendance_by_employee(
        employee_id
    )

    result = []

    for attendance in attendance_records:

        result.append({

            "id": str(attendance.id),
            "employee": str(attendance.employee.id),
            "date": attendance.date,
            "status": attendance.status
        })

    return result


# ============================================================
# Delete Attendance
# ============================================================

@router.delete("/attendance/{attendance_id}")
def remove_attendance(attendance_id: str):

    attendance = delete_attendance(
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

@router.post("/salary")
def add_salary(
    salary: MongoSalaryCreate
):

    new_salary = create_salary(
        salary
    )

    if not new_salary:

        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    return {

        "id": str(new_salary.id),
        "employee": str(new_salary.employee.id),
        "salary": new_salary.salary,
        "bonus": new_salary.bonus
    }


# ============================================================
# Get All Salaries
# ============================================================

@router.get("/salary")
def all_salaries():

    salary_records = get_salaries()

    result = []

    for salary in salary_records:

        result.append({

            "id": str(salary.id),
            "employee": str(salary.employee.id),
            "salary": salary.salary,
            "bonus": salary.bonus
        })

    return result


# ============================================================
# Get Salary By Employee
# ============================================================

@router.get("/salary/employee/{employee_id}")
def employee_salary(employee_id: str):

    salary_records = get_salary_by_employee(
        employee_id
    )

    result = []

    for salary in salary_records:

        result.append({

            "id": str(salary.id),
            "employee": str(salary.employee.id),
            "salary": salary.salary,
            "bonus": salary.bonus
        })

    return result


# ============================================================
# Delete Salary
# ============================================================

@router.delete("/salary/{salary_id}")
def remove_salary(salary_id: str):

    salary = delete_salary(
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
def search_employee(employee_name: str):

    employees = search_employee_by_name(
        employee_name
    )

    result = []

    for emp in employees:

        result.append({

            "id": str(emp.id),
            "name": emp.name,
            "age": emp.age,
            "email": emp.email,
            "phone": emp.phone,
            "designation": emp.designation
        })

    return result


# ============================================================
# Get High Salary Employees
# ============================================================

@router.get("/high-salary-employees")
def high_salary_employees(
    minimum_salary: float = 50000
):

    salaries = get_high_salary_employees(
        minimum_salary
    )

    result = []

    for salary in salaries:

        result.append({

            "employee_id": str(salary.employee.id),
            "employee_name": salary.employee.name,
            "salary": salary.salary,
            "bonus": salary.bonus
        })

    return result