'''
4. Product Rating Normalization
Ratings from different users:
ratings = np.array([2, 3, 4, 5, 1])
Task:
● Normalize ratings to a range 0 to 1 using:
normalized = (value - min) / (max - min)
'''

#importing numpy module
import numpy as np

#ratings from different users
ratings = np.array([2,3,4,5,1])
print(ratings)

#Normalize ratings to a range 0 to 1 using formula
normalized_rating = (ratings - np.min(ratings))/(np.max(ratings) - np.min(ratings))
print(np.round(normalized_rating, 2))

