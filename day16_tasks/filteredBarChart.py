'''
7. Filtered Bar Chart
Scenario:
marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]
Task:
● Convert to DataFrame
● Filter students with marks > 50
● Plot bar chart only for filtered students
'''

#importing modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#data
marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]

#converting into data frame
df = pd.DataFrame({"Names":names,"Marks":marks})
print(df)

#filter students with marks > 50
filtered_stu = df[df['Marks']> 50]
print(filtered_stu)

#creating bar chart
plt.bar(filtered_stu['Names'],height = filtered_stu['Marks'],width = 0.8, align = "center")
plt.title("Marks Analysis")
plt.xlabel("Student Names")
plt.ylabel("Marks Obtained")
plt.show()

