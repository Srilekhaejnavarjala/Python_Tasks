'''
9. Missing Data Handling (NumPy + Pandas)
A dataset:
arr = np.array([10, np.nan, 30, np.nan, 50])
Task:
● Convert to Pandas Series
● Replace NaN values with the mean of the Series
● Print updated data
'''

#importing modules
import numpy as np
import pandas as pd

#dataset
arr = np.array([10,np.nan,30,np.nan,50])
print("Numpy Array")
print(arr)
print(type(arr))
print("-------------------------------------------")

#converting into pandas
dataset = pd.Series(arr)
print("Pandas Series")
print(dataset)
print(type(dataset))
print("-------------------------------------------")

#Calculating mean value
mean_val = np.mean(dataset)
print("Mean of the given dataset is: ",mean_val)
print("-------------------------------------------")

#Replace NaN values with the mean of the series
updated_dataset = pd.Series(np.where(dataset.isnull(),mean_val,dataset))
print(updated_dataset)
