'''
5. Reshape & Row Averages
A dataset:
data = np.arange(1, 13)
Task:
● Reshape it into a 3×4 matrix
● Compute average of each row
'''

#importing numpy module
import numpy as np

#dataset
data = np.arange(1,13)

#reshaping dataset into 3X4 matrix
reshaped_data = np.reshape(data,shape =(3,4))
print("The Reshaped data: ")
print(reshaped_data)

#Computing average of each row
average_data = np.mean(reshaped_data,axis = 1)
print("The Average of 3X4 matrix row wise is: ")
print(average_data)

