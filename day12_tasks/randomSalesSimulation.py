'''
8. Random Sales Simulation
Scenario:
A company wants to simulate 10 days of sales (range 100–500).
Task:
● Generate random integers using NumPy.
● Print the array.
● Find the average sales.
'''

#importing numpy and random modules
import numpy as np
import random

#generating sales data
sales = np.random.random_integers(100,500,10)

#printing sales
print(sales)

#Average Calculation
total = sum(sales)
avg_sales_10days = total/10
print(f"The Average Sales of 10 days record is: {avg_sales_10days}")
