'''
 Sorting Product Prices
An e-commerce company stores product prices in a NumPy array.
Scenario:
Prices = [499, 299, 799, 199, 599]
Task:
● Convert it into a NumPy array.
● Sort the prices in ascending order.

'''

#importing numpy
import numpy as np

#prices
prices = [499,299,799,199,599]
print("The type of prices is: ",type(prices))

#converting it to numpy array
product_prices = np.array(prices)
print("The type of product prices is: ",type(product_prices))
print("Prices recorded before sorting is: ",product_prices)

#Sorting the prices in ascending order
print("The sorted product prices are: ",np.sort(product_prices))
