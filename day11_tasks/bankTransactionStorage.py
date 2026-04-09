'''
1. Bank Transaction Storage
A bank stores the transaction amounts of a customer in a list:
[1200, 500, 800, 1500]
Scenario:
● Convert the list into a NumPy array.
● Print the type of the object.
● Verify that it is a NumPy ndarray.
'''

#importing numpy
import numpy as np

#bank details
customer = [1200, 500, 800, 1500]

#converting it into array
amount = np.array(customer)

#printing the type of the list
print("The type of the list is: ",type(amount))

#verifying whether it is ndarray
if type(amount) == np.ndarray:
    print("This is a numpy ndarray.")
