'''
6. Row Selection & Deletion
A DataFrame:
df = pd.DataFrame({
"A": [10, 20, 30],
"B": [5, 15, 25]
}, index=["x", "y", "z"])
Task:
● Select row with index "y"
● Delete row "x"
● Print updated DataFrame
'''

#importing modules
import pandas as pd

#dataframe
df = pd.DataFrame({
"A": [10, 20, 30],
"B": [5, 15, 25]
}, index=["x", "y", "z"])
print("Data Frame: ")
print(df)
print("--------------------------------------------------------")

#Selecting row with index "y"
row = df.loc['y']
print("Row 'y' values:")
print(row)
print("--------------------------------------------------------")

#Deleting row "x" and printing updated data frame
df = df.drop('x')
print("Updated Data Frame: ")
print(df)
print("--------------------------------------------------------")


