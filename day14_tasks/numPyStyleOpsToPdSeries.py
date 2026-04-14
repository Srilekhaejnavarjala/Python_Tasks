'''
3. Add Constant to Series (NumPy Operation on Pandas)
A Series:
S = pd.Series([5, 10, 15])
Task:
● Add 5 to each element using NumPy-style operation
● Print updated Series
'''

#importing modules
import numpy as np
import pandas as pd

#data
S = pd.Series([5,10,15])
print("Original Series: ")
print(S)
print("-------------------------------------------------")

#Adding 5 to each element using NumPy style operation and printing it
updated_series = S+5
print("Updated Series: ")
print(updated_series)
