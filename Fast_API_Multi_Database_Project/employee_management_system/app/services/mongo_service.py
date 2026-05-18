# ============================================================
# MongoDB Services
# ============================================================

from app.models.mongo_models import Department


# ============================================================
# Create Department
# ============================================================

def create_department(data):

    department = Department(

        name=data.name,
        location=data.location
    )

    department.save()

    return department


# ============================================================
# Get All Departments
# ============================================================

def get_departments():

    return Department.objects()


# ============================================================
# Get Department By ID
# ============================================================

def get_department_by_id(department_id):

    return Department.objects(id=department_id).first()


# ============================================================
# Delete Department
# ============================================================

def delete_department(department_id):

    department = Department.objects(
        id=department_id
    ).first()

    if not department:
        return None

    department.delete()

    return department

# ============================================================
# Employee Services
# ============================================================

from app.models.mongo_models import Employee


# ============================================================
# Create Employee
# ============================================================

def create_employee(data):

    # Find Department
    department = Department.objects(
        id=data.department_id
    ).first()

    if not department:
        return None

    employee = Employee(

        name=data.name,
        age=data.age,
        email=data.email,
        phone=data.phone,
        designation=data.designation,
        department=department
    )

    employee.save()

    return employee


# ============================================================
# Get All Employees
# ============================================================

def get_employees():

    return Employee.objects()


# ============================================================
# Get Employee By ID
# ============================================================

def get_employee_by_id(employee_id):

    return Employee.objects(
        id=employee_id
    ).first()


# ============================================================
# Delete Employee
# ============================================================

def delete_employee(employee_id):

    employee = Employee.objects(
        id=employee_id
    ).first()

    if not employee:
        return None

    employee.delete()

    return employee

# ============================================================
# Attendance Services
# ============================================================

from app.models.mongo_models import Attendance


# ============================================================
# Create Attendance
# ============================================================

def create_attendance(data):

    # Find Employee
    employee = Employee.objects(
        id=data.employee_id
    ).first()

    if not employee:
        return None

    attendance = Attendance(

        employee=employee,
        date=data.date,
        status=data.status
    )

    attendance.save()

    return attendance


# ============================================================
# Get All Attendance
# ============================================================

def get_attendance():

    return Attendance.objects()


# ============================================================
# Get Attendance By Employee
# ============================================================

def get_attendance_by_employee(employee_id):

    employee = Employee.objects(
        id=employee_id
    ).first()

    if not employee:
        return []

    return Attendance.objects(
        employee=employee
    )


# ============================================================
# Delete Attendance
# ============================================================

def delete_attendance(attendance_id):

    attendance = Attendance.objects(
        id=attendance_id
    ).first()

    if not attendance:
        return None

    attendance.delete()

    return attendance

# ============================================================
# Salary Services
# ============================================================

from app.models.mongo_models import Salary


# ============================================================
# Create Salary
# ============================================================

def create_salary(data):

    # Find Employee
    employee = Employee.objects(
        id=data.employee_id
    ).first()

    if not employee:
        return None

    salary = Salary(

        employee=employee,
        salary=data.salary,
        bonus=data.bonus
    )

    salary.save()

    return salary


# ============================================================
# Get All Salaries
# ============================================================

def get_salaries():

    return Salary.objects()


# ============================================================
# Get Salary By Employee
# ============================================================

def get_salary_by_employee(employee_id):

    employee = Employee.objects(
        id=employee_id
    ).first()

    if not employee:
        return []

    return Salary.objects(
        employee=employee
    )


# ============================================================
# Delete Salary
# ============================================================

def delete_salary(salary_id):

    salary = Salary.objects(
        id=salary_id
    ).first()

    if not salary:
        return None

    salary.delete()

    return salary

# ============================================================
# Search Employee By Name
# ============================================================

def search_employee_by_name(employee_name):

    return Employee.objects(
        name__icontains=employee_name
    )


# ============================================================
# Get High Salary Employees
# ============================================================

def get_high_salary_employees(
    minimum_salary=50000
):

    return Salary.objects(
        salary__gte=minimum_salary
    )