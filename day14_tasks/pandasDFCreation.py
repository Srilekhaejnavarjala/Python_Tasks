'''
2. Basic DataFrame Creation from NumPy
You have:
data = np.array([[1, 2], [3, 4], [5, 6]])
Task:
● Convert it into a Pandas DataFrame
● Add column names: "X", "Y"
'''

#importing modules
import numpy as np
import pandas as pd

#data
data = np.array([[1,2],[3,4],[5,6]])
print("Numpy Array: ")
print(data)
print(type(data))
print("-----------------------------------------------")

#converting into pandas dataframe\
column_names = ["X","Y"]
data_frame = pd.DataFrame(data,columns = column_names)
print("Pandas Data Frame: ")
print(data_frame)
print(type(data_frame))
