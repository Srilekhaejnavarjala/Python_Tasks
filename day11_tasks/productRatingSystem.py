'''
Product Rating System
An e-commerce website stores product ratings:
[4, 5, 3, 4, 2]
Task:
● Convert it to a NumPy array.
● Print the first and last rating using indexing.
'''

#importing numpy
import numpy as np

#product ratings
product_ratings = [4,5,3,4,2]

#converting it to numpy array
store_product_ratings = np.array(product_ratings)
print("The given ratings are: ",store_product_ratings)

#printing first and last rating using indexing
print("The first rating given is: ",store_product_ratings[0])
print("The last rating given is: ",store_product_ratings[-1])
