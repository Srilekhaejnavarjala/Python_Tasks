'''
Replace Values Using Filtering
Scenario:
A dataset contains:
[5, 12, 18, 7, 25, 30]
Task:
● Replace all values greater than 15 with 0 using NumPy filtering.
'''

#importing numpy
import numpy as np

#dataset
data = [5,12,18,7,25,30]

#converting it into numpy array
values = np.array(data)
print("Original Array: ",values)

#filtering values greater than 15
values[values > 15] = 0
print("The filtered values of the array are: ",values)


