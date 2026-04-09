'''
7. Convert Float Prices to Integer
A shop stores product prices:
[10.5, 20.8, 15.3]
Scenario:
The billing system requires integer values.
Task:
● Convert the array from float to integer using astype()
'''

#importing numpy
import numpy as np

#product prices
prod_prices = [10.5,20.8,15.3]

#converting it to array
store_products = np.array(prod_prices)
print("Stored product prices in floating values: ")
print(store_products)

#converting type of values from float to integer
print("Stored product prices in integer values: ")
print(store_products.astype(int))
