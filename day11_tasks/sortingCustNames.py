'''
12. Sorting Customer Names
A system stores customer names:
["Ravi", "Anil", "Sita", "John"]
Task:
● Convert it to a NumPy array.
● Sort the names alphabetically.
'''

#importing numpy
import numpy as np

#customer names
customer_names = ["Ravi","Anil","Sita","John"]

#converting into numpy array
store_cust_names = np.array(customer_names)
print(store_cust_names)

#Sorting them alphabetically
sorted_names = np.sort(store_cust_names)
print("The sorted customer names are: \n",sorted_names)
