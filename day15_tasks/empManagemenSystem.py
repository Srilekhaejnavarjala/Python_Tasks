'''
5. Employee Management System (OOP + File + Dict)
Scenario:
Manage employee data.
Task:
● Create a class Employee
● Store employees in a dictionary
● Save data to a file
● Use exception handling for invalid salary input
● Use loop to display all employees
'''

#defining class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def employee_management(self):
        try:
            n = int(input("enter number of employees to store: "))
            emp_data = {}

            for i in range(n):
                name = input(f"enter employee {i+1} name: ")

                try:
                    salary = int(input("enter salary per month: "))
                except ValueError:
                    print("Invalid salary")
                    salary = 0

                emp = Employee(name, salary)
                emp_data[emp.name] = emp.salary

            print("Employees data:")
            print(emp_data)

            # Using loop to display all employees
            print("\nEmployee Names:")
            for name in emp_data:
                print(name)

            # Saving data into file
            choice = input("Do you want to store data in file? (Y/N) ")

            if choice.lower() == 'y':   # FIXED
                with open("employee_details.txt", 'a') as txt:
                    txt.write("Employee Details:\n")
                    for name, salary in emp_data.items():
                        txt.write(f"{name} : {salary}\n")
                    txt.write("\n")

                print("Data saved successfully")
            else:
                print("Sorry data cannot be saved into a file")

        except ValueError:
            print("The entered value must be an integer. Please try again")


# calling method
emp_obj = Employee("", 0)
emp_obj.employee_management()
    
