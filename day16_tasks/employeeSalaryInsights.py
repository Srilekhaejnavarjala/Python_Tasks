'''
3. Employee Salary Insights
Scenario:
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]
Task:
● Convert into DataFrame
● Plot:
○ Line graph → salary trend
○ Bar chart → department-wise salary comparison
○ Pie chart → department distribution
○ Histogram → salary distribution
○ Scatter plot → index vs salary
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#data
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

#DataFrame
df = pd.DataFrame({"Departments": departments, "Salaries": salaries})

#Subplots
fig, axes = plt.subplots(1,5, figsize=(20,5))

#Line (trend)
axes[0].plot(df.index, df['Salaries'])
axes[0].set_title("Salary Trend")

#Bar (aggregated)
dept_avg = df.groupby('Departments')['Salaries'].mean()
axes[1].bar(dept_avg.index, dept_avg.values)
axes[1].set_title("Avg Salary by Dept")

#Pie (aggregated)
dept_sum = df.groupby('Departments')['Salaries'].sum()
axes[2].pie(dept_sum, labels=dept_sum.index, autopct='%1.1f%%')
axes[2].set_title("Salary Distribution")

#Histogram
axes[3].hist(df['Salaries'], bins=5, edgecolor='black')
axes[3].set_title("Salary Distribution")

#Scatter
axes[4].scatter(df.index, df['Salaries'])
axes[4].set_title("Index vs Salary")

plt.tight_layout()
plt.show()
