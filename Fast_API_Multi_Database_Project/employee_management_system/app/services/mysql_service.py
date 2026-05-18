# ============================================================
# MySQL Service Layer
# ============================================================

from sqlalchemy.orm import Session

from app.models.sql_models import Department


# ============================================================
# Create Department
# ============================================================

def create_department(db: Session, department_data):

    new_department = Department(
        name=department_data.name,
        location=department_data.location
    )

    db.add(new_department)

    db.commit()

    db.refresh(new_department)

    return new_department


# ============================================================
# Get All Departments
# ============================================================

def get_departments(db: Session):

    return db.query(Department).all()


# ============================================================
# Get Department By ID
# ============================================================

def get_department_by_id(db: Session, department_id: int):

    return db.query(Department).filter(
        Department.id == department_id
    ).first()


# ============================================================
# Delete Department
# ============================================================

def delete_department(db: Session, department_id: int):

    department = db.query(Department).filter(
        Department.id == department_id
    ).first()

    if not department:
        return None

    db.delete(department)

    db.commit()

    return department

# ============================================================
# Employee Services
# ============================================================

from app.models.sql_models import Employee

# ============================================================
# Employee Services
# ============================================================

# ============================================================
# Create Employee
# ============================================================

def create_employee(db: Session, employee_data):

    new_employee = Employee(

        name=employee_data.name,
        age=employee_data.age,
        email=employee_data.email,
        phone=employee_data.phone,
        designation=employee_data.designation,
        department_id=employee_data.department_id
    )

    db.add(new_employee)

    db.commit()

    db.refresh(new_employee)

    return new_employee


# ============================================================
# Get All Employees
# ============================================================

def get_employees(db: Session):

    return db.query(Employee).all()


# ============================================================
# Get Employee By ID
# ============================================================

def get_employee_by_id(db: Session, employee_id: int):

    return db.query(Employee).filter(
        Employee.id == employee_id
    ).first()


# ============================================================
# Update Employee
# ============================================================

def update_employee(
    db: Session,
    employee_id: int,
    employee_data
):

    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if not employee:
        return None

    for key, value in employee_data.dict(exclude_unset=True).items():

        setattr(employee, key, value)

    db.commit()

    db.refresh(employee)

    return employee


# ============================================================
# Delete Employee
# ============================================================

def delete_employee(
    db: Session,
    employee_id: int
):

    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if not employee:
        return None

    db.delete(employee)

    db.commit()

    return employee

# ============================================================
# Search Employee By Name
# ============================================================

def search_employee_by_name(
    db: Session,
    employee_name: str
):

    return db.query(Employee).filter(
        Employee.name.ilike(f"%{employee_name}%")
    ).all()

# ============================================================
# Get High Salary Employees
# ============================================================

def get_high_salary_employees(
    db: Session,
    minimum_salary: float = 50000
):

    return db.query(Salary).filter(
        Salary.salary >= minimum_salary
    ).all()

# ============================================================
# Attendance Services
# ============================================================

from app.models.sql_models import Attendance


# ============================================================
# Create Attendance
# ============================================================

def create_attendance(
    db: Session,
    attendance_data
):

    new_attendance = Attendance(

        employee_id=attendance_data.employee_id,
        date=attendance_data.date,
        status=attendance_data.status
    )

    db.add(new_attendance)

    db.commit()

    db.refresh(new_attendance)

    return new_attendance


# ============================================================
# Get All Attendance
# ============================================================

def get_attendance(db: Session):

    return db.query(Attendance).all()


# ============================================================
# Get Attendance By Employee ID
# ============================================================

def get_attendance_by_employee(
    db: Session,
    employee_id: int
):

    return db.query(Attendance).filter(
        Attendance.employee_id == employee_id
    ).all()


# ============================================================
# Delete Attendance
# ============================================================

def delete_attendance(
    db: Session,
    attendance_id: int
):

    attendance = db.query(Attendance).filter(
        Attendance.id == attendance_id
    ).first()

    if not attendance:
        return None

    db.delete(attendance)

    db.commit()

    return attendance

# ============================================================
# Salary Services
# ============================================================

from app.models.sql_models import Salary


# ============================================================
# Create Salary Record
# ============================================================

def create_salary(
    db: Session,
    salary_data
):

    new_salary = Salary(

        employee_id=salary_data.employee_id,
        salary=salary_data.salary,
        bonus=salary_data.bonus
    )

    db.add(new_salary)

    db.commit()

    db.refresh(new_salary)

    return new_salary


# ============================================================
# Get All Salary Records
# ============================================================

def get_salaries(db: Session):

    return db.query(Salary).all()


# ============================================================
# Get Salary By Employee ID
# ============================================================

def get_salary_by_employee(
    db: Session,
    employee_id: int
):

    return db.query(Salary).filter(
        Salary.employee_id == employee_id
    ).all()


# ============================================================
# Delete Salary Record
# ============================================================

def delete_salary(
    db: Session,
    salary_id: int
):

    salary = db.query(Salary).filter(
        Salary.id == salary_id
    ).first()

    if not salary:
        return None

    db.delete(salary)

    db.commit()

    return salary