'''
5. Product Sales & Profit Analysis
Scenario:
sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]
Task:
● Create DataFrame
● Plot:
○ Line graph → sales trend
○ Bar chart → product vs sales
○ Pie chart → sales contribution
○ Histogram → profit distribution
○ Scatter plot → sales vs profit
'''

#importing modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#data
sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]

#Creating data frame
df = pd.DataFrame({"Products":products, "Sales":sales,"Profits":profit})
print(df)

fig, axes = plt.subplots(1,5,figsize = (20,5))

#Line graph
axes[0].plot(df['Products'],df['Sales'])
axes[0].set_title("Sales Trend")
axes[0].set_xlabel("Products")
axes[0].set_ylabel("Sales")

#Bar chart
axes[1].bar(df['Products'],df['Sales'])
axes[1].set_title("Product vs Sales")
axes[1].set_xlabel("Products")
axes[1].set_ylabel("Sales")

#Pie chart
axes[2].pie(df['Sales'],labels = df['Products'], autopct = '%1.1f%%')
axes[2].set_title("Product Distribution")

#Histogram
axes[3].hist(df['Profits'],bins = 5, edgecolor = 'black')
axes[3].set_title("Profit Distribution")
axes[3].set_xlabel("Profit")
axes[3].set_ylabel("Frequency")

#Scatter plot
axes[4].scatter(df['Sales'],df['Profits'])
axes[4].set_title("Sales vs Profit")
axes[4].set_xlabel("Sales")
axes[4].set_ylabel("Profits")

#displaying results
plt.tight_layout()
plt.show()
