#University Staff Management (Hierarchial Inheritance)
'''
A university has different staff types such as Professor, LabAssistant, and
Administrator. All inherit from a base class Staff. Implement hierarchical
inheritance to manage and display their information.

'''
class Staff:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
class Professor(Staff):
    def display(self):
        print("Professor Details: ")
        print("Name: ",self.name)
        print("Salary: ",self.salary)
        print()

class LabAssistant(Staff):
    def display(self):
        print("Lab Assistant Details: ")
        print("Name: ",self.name)
        print("Salary: ",self.salary)
        print()

class Administrator(Staff):
    def display(self):
        print("Administrator Details: ")
        print("Name: ",self.name)
        print("Salary: ",self.salary)
        print()
        
#creating objects
prof = Professor("Ramesh",80000)
lab = LabAssistant("Suresh",30000)
admin = Administrator("Mahesh",50000)

#displaying details
prof.display()
lab.display()
admin.display()

    
    
    
