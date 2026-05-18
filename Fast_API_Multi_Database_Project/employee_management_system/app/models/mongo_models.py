# ============================================================
# MongoDB Models
# ============================================================

from mongoengine import (
    Document,
    StringField,
    IntField,
    FloatField,
    DateField,
    ReferenceField
)


# ============================================================
# Department Collection
# ============================================================

class Department(Document):

    name = StringField(
        required=True,
        unique=True
    )

    location = StringField()

    meta = {
        "collection": "departments"
    }


# ============================================================
# Employee Collection
# ============================================================

class Employee(Document):

    name = StringField(required=True)

    age = IntField()

    email = StringField(unique=True)

    phone = StringField()

    designation = StringField()

    department = ReferenceField(Department)

    meta = {
        "collection": "employees"
    }


# ============================================================
# Attendance Collection
# ============================================================

class Attendance(Document):

    employee = ReferenceField(Employee)

    date = DateField()

    status = StringField()

    meta = {
        "collection": "attendance"
    }


# ============================================================
# Salary Collection
# ============================================================

class Salary(Document):

    employee = ReferenceField(Employee)

    salary = FloatField()

    bonus = FloatField()

    meta = {
        "collection": "salaries"
    }