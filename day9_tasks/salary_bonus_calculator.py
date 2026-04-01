#Employee Bonus Calculator (Decorators & OOOP)
'''
A company wants to apply a bonus calculation automatically before displaying the
salary. Create an Employee class and use a decorator that modifies the
salary by adding a bonus before displaying it.

'''
def add_bonus(func):

    def wrapper(self):
        bonus = 2000
        self.salary += bonus
        func(self)
    return wrapper

class Employee:
    
    def __init__(self):
        self.name = input("enter employee name: ")
        self.salary = int(input("enter salary: "))

    @add_bonus
    def display_salary(self):
        print("\n Employee details: ")
        print("Name: ",self.name)
        print("Salary after bonus: ",self.salary)

#creating object
emp = Employee()

#displaying result
emp.display_salary()
