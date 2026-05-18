# ============================================================
# SQLAlchemy Models
# ============================================================

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Date

from sqlalchemy.orm import relationship

# Import Base
from app.database.mysql import Base


# ============================================================
# Department Table
# ============================================================

class Department(Base):

    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), unique=True, nullable=False)

    location = Column(String(100))

    # Relationship
    employees = relationship("Employee", back_populates="department")


# ============================================================
# Employee Table
# ============================================================

class Employee(Base):

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    age = Column(Integer)

    email = Column(String(100), unique=True)

    phone = Column(String(20))

    designation = Column(String(100))

    department_id = Column(Integer, ForeignKey("departments.id"))

    # Relationships
    department = relationship("Department", back_populates="employees")

    attendance = relationship("Attendance", back_populates="employee")

    salary = relationship("Salary", back_populates="employee")


# ============================================================
# Attendance Table
# ============================================================

class Attendance(Base):

    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(Integer, ForeignKey("employees.id"))

    date = Column(Date)

    status = Column(String(20))

    # Relationship
    employee = relationship("Employee", back_populates="attendance")


# ============================================================
# Salary Table
# ============================================================

class Salary(Base):

    __tablename__ = "salaries"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(Integer, ForeignKey("employees.id"))

    salary = Column(Float)

    bonus = Column(Float)

    # Relationship
    employee = relationship("Employee", back_populates="salary")