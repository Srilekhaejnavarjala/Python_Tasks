'''
9. Reshaping Sales Data
A company stores monthly sales data:
[10,20,30,40,50,60,70,80,90,100,110,120]
Scenario:
You need to display the data as 4 months × 3 products matrix.
Task:
● Convert the list to NumPy array.
● Reshape it into a 4 × 3 array.
'''

#importing numpy
import numpy as np

#company data
store_data = [10,20,30,40,50,60,70,80,90,100,110,120]

#converting into numpy array
sales_data = np.array(store_data)
print("Sales data before reshaping \n", sales_data)

#converting into 4X3 matrix
reshaped_data = sales_data.reshape(4,3)
print("Reshaped sales data is \n",reshaped_data)
