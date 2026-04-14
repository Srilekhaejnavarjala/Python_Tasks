'''
8. Complex DataFrame Transformation
A DataFrame:
df = pd.DataFrame({
"Name": ["A", "B", "C", "D"],
"Marks": [50, 80, 30, 90]
})
Scenario:
● Students scoring below 50 failed
Task:
1. Create a column Status ("Pass"/"Fail")
2. Filter only passed students
3. Calculate average marks of passed student
'''

#importing module
import pandas as pd
import numpy as np

#data frame
df = pd.DataFrame({
"Name": ["A", "B", "C", "D"],
"Marks": [50, 80, 30, 90]
})
print("Data Frame: ")
print(df)
print("-------------------------------------------------------")

#creating column status
df['Status'] = np.where(df['Marks'] > 50,"Pass","Fail")
print(df)
print("-------------------------------------------------------")

#Filtering only passed students
passed_stu = df[df['Status']=="Pass"]
print("Students who passed the test are: ")
print(passed_stu)
print("-------------------------------------------------------")

#Calculating Average marks of passed students
average_marks = np.mean(passed_stu['Marks'])
print("The average marks of passed students is: ")
print(average_marks)
print("-------------------------------------------------------")

