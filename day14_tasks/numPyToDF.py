'''
8. Combine NumPy Arrays into DataFrame
Two arrays:
names = np.array(["A", "B", "C"])
marks = np.array([80, 90, 70])
Task:
● Create a DataFrame with columns "Name" and "Marks"
● Filter students with marks above 75
'''

#importing modules
import numpy as np
import pandas as pd

#two arrays
names = np.array(["A","B","C"])
marks = np.array([80,90,70])
print("Original Array: ")
print(names)
print(marks)
print("---------------------------------------------")

#creating a data frame with columns Name and Marks
headings = ["Name","Marks"]
student_marks = pd.DataFrame({'Names': names,'Marks': marks})
print(student_marks)

#Filtering students with marks above 75
updated_students = student_marks[student_marks['Marks']>75]
print("Students above 75 marks are: ")
print(updated_students)

