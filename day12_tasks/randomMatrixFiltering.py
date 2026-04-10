'''
10. Random Matrix and Condition Filtering
Scenario:
● Generate a 3×3 matrix of random numbers (0–50).
Task:
● Filter elements greater than 25.
● Print filtered values.
'''

#importing numpy
import numpy as np


#creating 3X3 matrix
matrix = np.random.randint(0,50,size = (3,3))
print(matrix)

#filtering elements greater than 25
filtered_matrix = matrix[matrix > 25]
print("Filtered Matrix: ",filtered_matrix)
