'''
4. Find Maximum Value
A dataset:
arr = np.array([12, 45, 22, 67, 34])
Task:
● Convert to Pandas Series
● Find the maximum value
'''

#importing modules
import numpy as np
import pandas as pd

#data
arr = np.array([12,45,22,67,34])
print("Numpy Array: ")
print(arr)
print(type(arr))

#converting numpy to pandas
series_data = pd.Series(arr)
print("Data Series: ")
print(series_data)
print(type(series_data))

#finding out maximum value from data frame
maximum_value = max(series_data)
print("The maximum value of the given data frame is: ",maximum_value)


