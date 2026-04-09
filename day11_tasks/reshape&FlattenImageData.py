'''
15. Reshape and Flatten Image Data
Scenario:
An image is stored as a 2 × 3 matrix:
[[1,2,3],
[4,5,6]]
Task:
1. Convert it into a NumPy array.
2. Flatten the array into 1-D format.
3. Print the flattened array.
'''

#importing numpy
import numpy as np

#data
d_1 = [1,2,3]
d_2 = [4,5,6]

#creating into numpy
data = np.array([d_1,d_2])
print(data)

#flattening array into 1D format
print("The flattened array is: ")
reshaped_data = data.reshape(-1)
print(reshaped_data)
