'''
6. Check Data Type of Inventory Values
A warehouse stores product quantities:
[10, 20, 30, 40]
Task:
● Convert it into a NumPy array.
● Print the data type (dtype) of the array.
'''

#importing numpy
import numpy as np

#warehouse stores product quantities
prod_quantity = [10,20,30,40]

#converting into numpy array
warehouse_prod_quan = np.array(prod_quantity)
print(warehouse_prod_quan)

#printing data type of array
print("The data type of the array is: ",warehouse_prod_quan.dtype)

