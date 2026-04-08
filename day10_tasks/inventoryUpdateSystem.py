'''
8. Inventory Update System
A warehouse has an inventory stored in a matrix.
[[10, 15],
[20, 25]]
Scenario:
A new shipment increases every item quantity by 2 units.
Task:
● Add 2 to every element using NumPy.
● Print the updated inventor
'''

#importing numpy
import numpy as np

#warehouse data
inventory_data = np.array([[10,15],[20,25]])
print("The inventory stock data is: ",inventory_data)

#Shipment increase update and printing
new_shipment_data = inventory_data + 2
print(f"The new shipment data after increasing quantity is : {new_shipment_data}")

