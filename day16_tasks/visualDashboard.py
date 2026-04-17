'''
9. Combined Visualization Dashboard
Scenario:
sales = np.array([100, 200, 150, 300])
products = ["A", "B", "C", "D"]
Task:
● Create DataFrame
● Plot:
○ Line graph (trend)
○ Bar chart (comparison)
○ Pie chart (distribution)
● Show all in single figure (subplots)
'''

#importing modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#data
sales = np.array([100, 200, 150, 300])
products = ["A", "B", "C", "D"]

#creating data frame
df = pd.DataFrame({"Products": products, "Sales": sales})

#creating subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

#1. Line graph
axes[0].plot(df['Products'], df['Sales'])
axes[0].set_title("Line Chart")
axes[0].set_xlabel("Products")
axes[0].set_ylabel("Sales")

#2. Bar chart
axes[1].bar(df['Products'], df['Sales'])
axes[1].set_title("Bar Chart")
axes[1].set_xlabel("Products")
axes[1].set_ylabel("Sales")

#3. Pie chart
axes[2].pie(df['Sales'], labels=df['Products'], autopct='%1.1f%%')
axes[2].set_title("Pie Chart")

#main title
plt.suptitle("Combined Visualization Dashboard")

plt.tight_layout()
plt.show()
