'''
3. Accessing Specific Data (Indexing)
A Series contains:
S = pd.Series([100, 200, 300, 400], index=["A", "B", "C", "D"])
Task:
● Access values for B and D
● Return them as a subset
'''

#importing module
import pandas as pd
import numpy as np


#Series data
S = pd.Series([100, 200, 300, 400], index=["A", "B", "C", "D"])
print(S)
print(type(S))
print("----------------------------------------------------------")

#Accessing values for B and D
b_val = S["B"]
d_val = S["D"]
print(f"The value for index B is {b_val}. ")
print(f"The value for index D is {d_val}.")
print("----------------------------------------------------------")

#returning them as subset
subset = S[["B","D"]]
print("Subset of the given Series is: ")
print(subset)
