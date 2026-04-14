'''
10. Row Filtering + Aggregation
A dataset:
arr = np.array([
[100, 200],
[150, 250],
[80, 120],
[300, 400]
])
Task:
● Convert to DataFrame with columns "Sales", "Profit"
● Filter rows where Sales > 100
● Find average Profit of filtered rows.
'''

#importing modules
import numpy as np
import pandas as pd

#dataset
arr = np.array([
[100, 200],
[150, 250],
[80, 120],
[300, 400]
])
print("Numpy Array: ")
print(arr)
print("-------------------------------------------------")

#converting into data frame
series_data = pd.DataFrame(arr,columns = ["Sales","Profit"])
print("Pandas Data Frame: ")
print(series_data)
print("-------------------------------------------------")

#filter rows where Sales > 100
filtered_rows = series_data[series_data['Sales'] > 100]
print("Sales greater than 100 are: ")
print(filtered_rows)
print("-------------------------------------------------")

#Find average profit of filtered rows
average_rows = np.mean(filtered_rows['Profit'])
print("Average Profit of Sales greater than 100 are: ")
print(average_rows)
