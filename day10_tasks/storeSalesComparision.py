'''
Store Sales Comparison
Two stores record daily sales for 3 days.
Scenario:
Store A = [200, 250, 300]
Store B = [180, 270, 310]
Task:
● Store them in NumPy arrays.
● Find the daily difference in sales between the two stores.
● Print the resulting array.

'''

#importing numpy
import numpy as np

#store data
store_A = [200,250,300]
store_B = [180,270,310]

#converting into numpy arrays
store_A_data = np.array(store_A)
store_B_data = np.array(store_B)
print("Store A: ",store_A_data)
print("Store B: ",store_B_data)

#finding daily difference in sales between two stores
difference_of_stores = store_A_data - store_B_data
print(f"The daily difference in sales between two stores is: {difference_of_stores}")



