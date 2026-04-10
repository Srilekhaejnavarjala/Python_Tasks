'''
11. Boolean Masking for Salary Analysis
Scenario:
Employee salaries:
[25000, 40000, 15000, 50000, 30000]
Task:
● Filter salaries above 30000.
● Count how many employees satisfy this condition.
'''

#importing numpy
import numpy as np

#employee salaries data
salaries = [25000,40000,15000,50000,30000]

#creating numpy array
emp_salaries = np.array(salaries)
print(emp_salaries)

#filtering salaries above 30000
highest_salaries = emp_salaries > 30000
print("Employees with highest salary are: ")
print(highest_salaries)
count = np.sum(highest_salaries)
print(f"Total employees with salary more than 30000 are {count}")
