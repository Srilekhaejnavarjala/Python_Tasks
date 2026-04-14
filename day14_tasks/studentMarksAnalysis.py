'''
6. Student Marks Analysis (NumPy ----> Pandas)
Marks data:
arr = np.array([
[80, 90],
[70, 60],
[85, 95]
])
Task:
● Convert into DataFrame with columns "Math", "Science"
● Add a new column Total
● Find student with highest total
'''

#importing modules
import numpy as np
import pandas as pd

#marks data
arr = np.array([
[80, 90],
[70, 60],
[85, 95]
])
print("Numpy Array: ")
print(arr)
print(type(arr))
print("------------------------------------------")

#converting into pandas data frame
subjects = ["Math","Science"]
student_marks = pd.DataFrame(arr,columns = subjects)
print("Data Frame: ")
print(student_marks)
print(type(student_marks))
print("------------------------------------------")

#adding a new column total
student_marks['Total'] = student_marks.sum(axis = 1)
print(student_marks)

