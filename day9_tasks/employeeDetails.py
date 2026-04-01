#Employee Salary System
'''
A company has two types of employees: Employee and Manager. Create a base
class Employee containing name and salary. Create a derived class Manager
that inherits from Employee and displays the employee details.

'''

class Employee:
    def __init__(self):
        self.n = int(input("enter number of employees: "))
        self.employees = []
        for i in range(1,self.n+1):
            self.type_of_employee = input("enter type of employee: ")
            self.name = input("enter name of employee: ")
            self.salary = int(input("enter salary of employee: "))
            self.employees.append((self.type_of_employee,self.name,self.salary))

class Manager(Employee):
    def display_details(self):
        print("The employee details are: ")
#Employee Salary System
'''
A company has two types of employees: Employee and Manager. Create a base
class Employee containing name and salary. Create a derived class Manager
that inherits from Employee and displays the employee details.

'''

class Employee:
    def __init__(self):
        self.n = int(input("enter number of employees: "))
        for i in range(1,self.n+1):
            self.type_of_employee = input("enter type of employee: ")
            self.name = input("enter name of employee: ")
            self.salary = int(input("enter salary of employee: "))

class Manager(Employee):
    def display_details(self):
        print("The employee details are: ")
        print("---------------------------------------------------\n")
        print(f"Type of Employee: {self.type_of_employee}")
        print(f"Name of Employee: {self.name}")
        print(f"Salary of Employee: {self.salary}")
        print("---------------------------------------------------\n")


    
#creating object
emp = Manager()

#displaying employee details
emp.display_details()
        for emp in self.employees:
            print(f"Type of Employee: {self.type_of_employee}")
            print(f"Name of Employee: {self.name}")
            print(f"Salary of Employee: {self.salary}")
            print("---------------------------------------------------\n")


    
#creating object
emp = Manager()

#displaying employee details
emp.display_details()
