'''
7. Data Alignment Issue in Series Addition
Two Series:
S1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])
Task:
● Add both Series
● Explain why some values become NaN
● Replace NaN with 0 and compute final result
'''

#importing module
import pandas as pd

#data series
S1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])
print("Series 1: ")
print(S1)
print("-------------------------------------------------------")
print("Series 2: ")
print(S2)
print("-------------------------------------------------------")

#Adding both series
series = S1 + S2
print("Cumulative Series are: ")
print(series)
print("-------------------------------------------------------")

#Finding out NaN values
nan_vals = series[series.isnull()].index
print("NaN values are at the rows: ")
print(nan_vals)
print("-------------------------------------------------------")

#Replacing NaN with 0 and computing final result
updated_vals = series.fillna(0)
print(updated_vals)
