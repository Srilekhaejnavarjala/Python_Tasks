'''
1. Student Performance Dashboard
Scenario:
A school records marks of students in one subject:
marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]
Task:
● Convert to Pandas DataFrame
● Plot:
○ Line graph → trend of marks
○ Bar chart → student vs marks
○ Pie chart → Pass (>50) vs Fail
○ Histogram → distribution of marks
○ Scatter plot → index vs marks
'''

#importing modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#data
marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

#coverting into pandas df
df = pd.DataFrame({"Students":students, "Marks":marks})
print(df)

#calculating pass and fail
df['Status'] = np.where(df['Marks'] > 50,"Pass","Fail")
print(df)

fig,axes = plt.subplots(1,5, figsize = (20,5))

#Plotting graphs
axes[0].plot(df['Students'],df['Marks'])
axes[0].set_title("Trend of Marks")
axes[0].set_xlabel("Students")
axes[0].set_ylabel("Marks")

#Bar chart
axes[1].bar(df['Students'],df['Marks'])
axes[1].set_title("Student Vs Marks")
axes[1].set_xlabel("Student")
axes[1].set_ylabel("Marks")

#Pie chart
counts = df['Status'].value_counts()
axes[2].pie(counts,labels = counts.index, autopct = '%1.1f%%')
axes[2].set_title("Pass vs Fail")

#Histogram
axes[3].hist(df['Marks'], bins = 10, edgecolor = 'black')
axes[3].set_title("Distribution of Marks")
axes[3].set_xlabel("Students")
axes[3].set_ylabel("Marks")

#Scatter plot
axes[4].scatter(df.index, df['Marks'])
axes[4].set_title("Index vs Marks")
axes[4].set_xlabel("Index")
axes[4].set_ylabel("Marks")

#displaying results
plt.show()
