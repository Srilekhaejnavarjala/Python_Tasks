# ============================================================
# IMPORTS
# ============================================================

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

import requests

from flask import session
from sqlalchemy import and_
from datetime import datetime

# ============================================================
# FLASK APP
# ============================================================

app = Flask(__name__)
app.secret_key = "hrms_secret_key"

# ============================================================
# FASTAPI BACKEND URL
# ============================================================

FASTAPI_URL = "http://127.0.0.1:8000"



@app.route("/")
def home():

    return redirect(url_for("login"))
# ============================================================
# LOGIN PAGE
# ============================================================

@app.route("/login", methods=["GET", "POST"])
def login():

    departments = requests.get(
        f"{FASTAPI_URL}/departments"
    ).json()

    if request.method == "POST":

        email = request.form["email"]

        designation = request.form["designation"]

        department_id = int(
            request.form["department_id"]
        )

        employees = requests.get(
            f"{FASTAPI_URL}/employees"
        ).json()

        valid_employee = None

        for employee in employees:

            if (
                employee["email"] == email
                and employee["designation"] == designation
                and employee["department_id"] == department_id
            ):

                valid_employee = employee
                break

        if valid_employee:

            session["employee_name"] = (
                valid_employee["name"]
            )

            session["designation"] = (
                valid_employee["designation"]
            )

            session["department_id"] = (
                valid_employee["department_id"]
            )

            return redirect(url_for("dashboard"))

        return render_template(
            "auth/login.html",
            departments=departments,
            error="Access Denied"
        )

    return render_template(
        "auth/login.html",
        departments=departments,
        error=None
    )

# ============================================================
# DASHBOARD HOME
# ============================================================

@app.route("/dashboard")
def dashboard():

    # Check Login
    if "employee_name" not in session:

        return redirect(url_for("login"))

    employees = requests.get(
        f"{FASTAPI_URL}/employees"
    ).json()

    departments = requests.get(
        f"{FASTAPI_URL}/departments"
    ).json()

    attendance = requests.get(
        f"{FASTAPI_URL}/attendance"
    ).json()

    salaries = requests.get(
        f"{FASTAPI_URL}/salary"
    ).json()

    designation = session.get("designation")

    department_id = session.get("department_id")

    # ====================================================
    # ADMIN ACCESS
    # ====================================================

    if designation.lower() == "admin":

        filtered_employees = employees

    # ====================================================
    # HR / PROJECT LEAD ACCESS
    # ====================================================

    else:

        filtered_employees = [

            employee

            for employee in employees

            if employee["department_id"] == department_id
        ]

    return render_template(
        "dashboard/index.html",
        employees=filtered_employees,
        departments=departments,
        attendance=attendance,
        salaries=salaries,
        employee_name=session.get("employee_name"),
        designation=designation
    )

# ============================================================
# EMPLOYEES PAGE
# ============================================================

@app.route("/employees")
def employees():

    if "employee_name" not in session:

        return redirect(url_for("login"))

    employees = requests.get(
        f"{FASTAPI_URL}/employees"
    ).json()

    departments = requests.get(
        f"{FASTAPI_URL}/departments"
    ).json()

    designation = session.get("designation")

    department_id = session.get("department_id")

    # ====================================================
    # ADMIN CAN SEE ALL
    # ====================================================

    if designation.lower() == "admin":

        filtered_employees = employees

    # ====================================================
    # OTHERS SEE ONLY THEIR DEPARTMENT
    # ====================================================

    else:

        filtered_employees = [

            employee

            for employee in employees

            if employee["department_id"] == department_id
        ]

    return render_template(

        "employees/employees.html",

        employees=filtered_employees,

        departments=departments
    )

# ============================================================
# ADD EMPLOYEE PAGE
# ============================================================

@app.route("/add-employee", methods=["GET", "POST"])
def add_employee():

    departments = requests.get(
        f"{FASTAPI_URL}/departments"
    ).json()

    if request.method == "POST":

        employee_data = {

            "name": request.form["name"],

            "age": int(
                request.form["age"]
            ),

            "email": request.form["email"],

            "phone": request.form["phone"],

            "designation": request.form["designation"],

            "department_id": int(
                request.form["department_id"]
            )
        }

        requests.post(
            f"{FASTAPI_URL}/employees",
            json=employee_data
        )

        return redirect(
            url_for("employees")
        )

    return render_template(
        "employees/add_employee.html",
        departments=departments
    )


# ============================================================
# DELETE EMPLOYEE
# ============================================================

@app.route("/delete-employee/<int:employee_id>")
def delete_employee(employee_id):

    requests.delete(
        f"{FASTAPI_URL}/employees/{employee_id}"
    )

    return redirect(
        url_for("employees")
    )


# ============================================================
# ATTENDANCE PAGE
# ============================================================

@app.route("/attendance")
def attendance():

    # Logged in user department
    user_department = session.get("department_id")

    # Logged in user designation
    user_designation = session.get("designation")

    # Selected date
    selected_date = request.args.get("selected_date")

    # Fetch attendance
    attendance_data = requests.get(
        f"{FASTAPI_URL}/attendance"
    ).json()

    # Fetch employees
    employees = requests.get(
        f"{FASTAPI_URL}/employees"
    ).json()

    filtered_attendance = []

    # ========================================================
    # FILTER EMPLOYEES BY DEPARTMENT
    # ========================================================

    department_employees = []

    for emp in employees:

        if emp["department_id"] == user_department:

            department_employees.append(emp)

    # ========================================================
    # BUILD ATTENDANCE VIEW
    # ========================================================

    for emp in department_employees:

        employee_attendance = None

        for record in attendance_data:

            if (
                record["employee_id"] == emp["id"]
            ):

                # Date filter
                if selected_date:

                    if record["date"] != selected_date:
                        continue

                employee_attendance = record
                break

        # If attendance exists
        if employee_attendance:

            filtered_attendance.append({

                "employee_name": emp["name"],

                "status": employee_attendance["status"],

                "date": employee_attendance["date"]

            })

        # If no attendance found
        else:

            filtered_attendance.append({

                "employee_name": emp["name"],

                "status": "not marked",

                "date": selected_date if selected_date else "N/A"

            })

    # ========================================================
    # COUNTS
    # ========================================================

    present_count = len([
        r for r in filtered_attendance
        if r["status"].lower() == "present"
    ])

    absent_count = len([
        r for r in filtered_attendance
        if r["status"].lower() == "absent"
    ])

    leave_count = len([
        r for r in filtered_attendance
        if r["status"].lower() == "leave"
    ])

    return render_template(
        "attendance/attendance.html",
        attendance=filtered_attendance,
        present_count=present_count,
        absent_count=absent_count,
        leave_count=leave_count,
        selected_date=selected_date
    )
# ============================================================
# ATTENDANCE FILTER API
# ============================================================

@app.get("/attendance-filter")
def attendance_filter(
    attendance_date: str,
    department_id: int
):

    db = SessionLocal()

    # ========================================================
    # GET EMPLOYEES FROM DEPARTMENT
    # ========================================================

    employees = db.query(Employee).filter(
        Employee.department_id == department_id
    ).all()

    employee_ids = [
        employee.id
        for employee in employees
    ]

    # ========================================================
    # GET ATTENDANCE RECORDS
    # ========================================================

    attendance_records = db.query(attendance).filter(

        and_(

            attendance.employee_id.in_(employee_ids),
            Attendance.date == datetime.strptime(attendance_date, "%Y-%m-%d").date()
            )

    ).all()

    # ========================================================
    # CLASSIFICATION
    # ========================================================

    present = []

    absent = []

    leave = []

    for record in attendance_records:

        employee = db.query(Employee).filter(
            Employee.id == record.employee_id
        ).first()

        employee_data = {

            "id": employee.id,

            "name": employee.name,

            "designation": employee.designation,

            "email": employee.email,

            "status": record.status
        }

        # ====================================================
        # STATUS LOGIC
        # ====================================================

        if record.status.lower() == "present":

            present.append(employee_data)

        elif record.status.lower() == "absent":

            absent.append(employee_data)

        elif record.status.lower() == "leave":

            leave.append(employee_data)

    # ========================================================
    # RESPONSE
    # ========================================================

    return {

        "present_count": len(present),
        "absent_count": len(absent),
        "leave_count": len(leave),
        "present_employees": present,
        "absent_employees": absent,
        "leave_employees": leave
    }

# ============================================================
# PAYROLL PAGE
# ============================================================

@app.route("/payroll")
def payroll():

    salaries = requests.get(
        f"{FASTAPI_URL}/salary"
    ).json()

    employees = requests.get(
        f"{FASTAPI_URL}/employees"
    ).json()

    return render_template(
        "salary/payroll.html",
        salaries=salaries,
        employees=employees
    )


# ============================================================
# ANALYTICS PAGE
# ============================================================

@app.route("/analytics")
def analytics():

    employees = requests.get(
        f"{FASTAPI_URL}/employees"
    ).json()

    departments = requests.get(
        f"{FASTAPI_URL}/departments"
    ).json()

    attendance = requests.get(
        f"{FASTAPI_URL}/attendance"
    ).json()

    salaries = requests.get(
        f"{FASTAPI_URL}/salary"
    ).json()

    # ========================================================
    # DEPARTMENT DISTRIBUTION
    # ========================================================

    department_labels = []
    department_counts = []

    for dept in departments:

        department_labels.append(dept["name"])

        count = len([
            emp for emp in employees
            if emp["department_id"] == dept["id"]
        ])

        department_counts.append(count)

    # ========================================================
    # ATTENDANCE COUNTS
    # ========================================================

    present_count = len([
        a for a in attendance
        if a["status"].lower() == "present"
    ])

    absent_count = len([
        a for a in attendance
        if a["status"].lower() == "absent"
    ])

    leave_count = len([
        a for a in attendance
        if a["status"].lower() == "leave"
    ])

    # ========================================================
    # SALARY ANALYTICS
    # ========================================================

    salary_labels = []
    salary_values = []

    for dept in departments:

        dept_employees = [
            emp["id"]
            for emp in employees
            if emp["department_id"] == dept["id"]
        ]

        dept_salaries = [
            sal["salary"]
            for sal in salaries
            if sal["employee_id"] in dept_employees
        ]

        avg_salary = (
            sum(dept_salaries) / len(dept_salaries)
            if dept_salaries else 0
        )

        salary_labels.append(dept["name"])
        salary_values.append(avg_salary)

    return render_template(
        "analytics/analytics.html",

        employees=employees,
        departments=departments,
        attendance=attendance,
        salaries=salaries,

        department_labels=department_labels,
        department_counts=department_counts,

        present_count=present_count,
        absent_count=absent_count,
        leave_count=leave_count,

        salary_labels=salary_labels,
        salary_values=salary_values
    )

# ============================================================
# SEARCH EMPLOYEE
# ============================================================

@app.route("/search")
def search():

    query = request.args.get("query")

    if not query:

        return redirect(
            url_for("employees")
        )

    employees = requests.get(
        f"{FASTAPI_URL}/search-employee/{query}"
    ).json()

    return render_template(
        "employees/employees.html",
        employees=employees
    )


# ============================================================
# EMPLOYEE PROFILE PAGE
# ============================================================

@app.route("/employee/<int:employee_id>")
def employee_profile(employee_id):

    employees = requests.get(
        f"{FASTAPI_URL}/employees"
    ).json()

    employee = None

    for emp in employees:

        if emp["id"] == employee_id:

            employee = emp
            break

    if not employee:

        return "Employee Not Found"

    # ==========================================
    # DUMMY ENTERPRISE DATA
    # ==========================================

    employee["experience"] = "4 Years"

    employee["performance"] = 92

    employee["attendance_score"] = 96

    employee["productivity"] = 89

    employee["manager"] = "Robert Williams"

    employee["skills"] = [

        "Python",
        "SQL",
        "FastAPI",
        "Flask",
        "Leadership"
    ]

        # ==========================================
    # TASKS / TIMESHEET
    # ==========================================

    employee["tasks"] = [

        {
            "task": "API Development",
            "status": "Completed",
            "hours": 5
        },

        {
            "task": "Dashboard UI",
            "status": "In Progress",
            "hours": 3
        },

        {
            "task": "Attendance Module",
            "status": "Pending",
            "hours": 2
        },

        {
            "task": "Analytics Charts",
            "status": "Completed",
            "hours": 4
        }

    ]

    return render_template(
        "employees/profile.html",
        employee=employee
    )
# ============================================================
# LOGOUT
# ============================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))

# ============================================================
# RUN FLASK APP
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )