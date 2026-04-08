'''
Matrix Transformation in Image Processing
An image processing system stores pixel intensity values in a matrix.
Scenario:
[[1,2],
 [3,4]]

Task:
● Create a NumPy array for this matrix.
● Find its transpose.
● Print both matrices.
'''

#importing numpy
import numpy as np

#matrix values
mat_1 = [1,2]
mat_2 = [3,4]

#converting into numpy arrays
pixel_data = np.array([mat_1,mat_2])
print("The image pixel data is: \n",pixel_data)
print("The shape of matrix before transpose is: ",np.shape(pixel_data))

#transposing the data
transpose_pixel_data = np.transpose(pixel_data)
print("The transpose of pixel data is: \n",transpose_pixel_data)
print("The shape of matrix after transpose is: ",np.shape(transpose_pixel_data))
