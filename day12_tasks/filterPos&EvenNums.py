'''
7. Filter Positive Even Numbers from Dataset
Scenario:
A dataset contains mixed values:
arr = [-5, 10, 15, -2, 20, 25, 30]
Task:
● Convert to NumPy array.
● Filter values that are:
○ Positive
○ Even
'''

#importing numpy
import numpy as np

#dataset
arr = [-5, 10, 15, -2, 20, 25, 30]

#converting into numpy
arr = np.array(arr)

#filtering numbers
positive_nums = arr[arr > 0]
even_nums = arr[arr % 2 == 0]

#printing lists
print("Original Array: ",arr)
print("Positive Nums List: ",positive_nums)
print("Even Nums List: ",even_nums)

