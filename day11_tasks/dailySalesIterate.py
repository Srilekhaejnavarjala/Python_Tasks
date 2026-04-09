'''
8. Iterate Through Daily Sales
Daily sales data:
[200, 300, 150, 400]
Task:
● Store it in a NumPy array.
● Iterate through the array and print each sale value.
'''

#importing numpy
import numpy as np

#daily sales data
daily_data = [200,300,150,400]

#converting it to numpy
sales_data = np.array(daily_data)
print(sales_data)

#iterating through array and printing each value
for data in sales_data:
    print(data)
