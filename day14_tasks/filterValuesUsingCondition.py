'''
5. Filter Values Using Condition
A dataset:
arr = np.array([10, 25, 30, 15, 40])
Task:
● Convert to Pandas Series
● Filter values greater than 20
'''

#importing modules
import numpy as np
import pandas as pd

#numpy array
arr = np.array([10,25,30,15,40])
print("Numpy Array: ")
print(arr)
print(type(arr))
print("------------------------------------------")

#converting it into pandas series
series_arr = pd.Series(arr)
print("Series Array: ")
print(series_arr)
print(type(series_arr))
print("------------------------------------------")

#filtering values greater than 20
filtered_arr = series_arr[series_arr > 20]
print("Filtered Array : ")
print(filtered_arr)
