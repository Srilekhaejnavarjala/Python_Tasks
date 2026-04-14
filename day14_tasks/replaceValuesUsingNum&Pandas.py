'''
7. Replace Values Using NumPy + Pandas
A Series:
S = pd.Series([10, 50, 30, 80, 20])
Task:
● Replace values greater than 40 with 0 using NumPy logic
● Return updated Series
'''

#importing modules
import numpy as np
import pandas as pd

#series data
S = pd.Series([10,50,30,80,20])
print("Original Series: ")
print(S)
print("---------------------------------------------------")

#Replace values greater than 40 with 0 using Numpy logic and printing them
updated_series = pd.Series(np.where(S>40,0,S))
print("The updated series are: ")
print(updated_series)
