'''
1. Convert NumPy array to Pandas Series
A dataset:
arr = np.array([10, 20, 30, 40])
Task:
● Convert this NumPy array into a Pandas Series
● Assign index labels: ["A", "B", "C", "D"]

'''

#importing packages
import numpy as np
import pandas as pd

#dataset
data = np.array([10,20,30,40])
print("Numpy Array: ")
print(data)
print(type(data))
print("--------------------------------------")

#converting numpy into pandas series
labels = ["A","B","C","D"]
series_data = pd.Series(data, index = labels)
print("Pandas Series: ")
print(series_data)
print(type(series_data))

