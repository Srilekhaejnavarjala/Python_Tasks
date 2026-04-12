'''
1. Sales threshold filtering
You are given monthly sales:
sales = np.array([12000, 18000, 22000, 15000, 30000])
Task:
● Filter all sales values greater than the average sales
● Return the filtered array.
'''

#importing numpy module
import numpy as np

#Sales array
sales = np.array([12000, 18000, 22000, 15000, 30000])
print(sales)

#Calculating average sales
total_sales = np.sum(sales)
average_sales = total_sales/len(sales)
print("The average sales of the given sales is: ",average_sales)

#Filtering all sales values greater than average sales
filtered_sales = sales[sales > average_sales]
print("Sales which are more than threshold value is: ")
print(filtered_sales)
