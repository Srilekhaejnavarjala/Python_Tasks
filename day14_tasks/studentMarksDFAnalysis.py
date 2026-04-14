'''
4. Student Marks Data Frame Analysis
A DataFrame:
data = pd.DataFrame({
"Name": ["A", "B", "C"],
"Math": [80, 70, 60],
"Science": [90, 60, 70]
})
Task:
● Add a new column Total = Math + Science
● Find the student with the highest total marks
'''

#importing module
import pandas as pd

#dataframe
data = pd.DataFrame({
"Name": ["A", "B", "C"],
"Math": [80, 70, 60],
"Science": [90, 60, 70]
})
print(data)
print("---------------------------------------------------------")

#Add a new column total = Math + Science
data['Total'] = data['Math']+data['Science']
print(data)
print("---------------------------------------------------------")

#Find the student with the highest total marks
highest_marks = max(data['Total'])
print(f"Highest Marks of the given list is: {highest_marks} ")

