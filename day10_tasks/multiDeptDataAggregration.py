'''
9. Multi-Department Data Aggregation
A company collects employee counts from two branches.
Branch A:
[[10, 20],
[30, 40]]
Branch B:
[[5, 15],
[25, 35]]
Scenario:
● Combine the two matrices.
● Calculate the total employees across all departments.
● Print the combined matrix and total.
'''

#importing numpy
import numpy as np

#employee data
branch_A = np.array([[10,20],[30,40]])
branch_B = np.array([[5,15],[25,35]])

#combining two matrices
combined_branch = branch_A + branch_B
print("The combined matrix is: ",combined_branch)

#calculate total employee across all departments
total_employees = np.sum(combined_branch)
print("Total employees across all departments is: ")
print(total_employees)
