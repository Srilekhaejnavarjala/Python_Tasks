'''
2. Monthly Sales Analysis
Scenario:
sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
Task:
● Create DataFrame
● Plot:
○ Line graph → sales trend
○ Bar chart → month-wise comparison
○ Pie chart → contribution of each month
○ Histogram → frequency of sales values
○ Scatter plot → month index vs sales
'''

#importing modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#data
sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

#Creating data frame
df = pd.DataFrame({"Months":months,"Sales":sales})
print(df)

#creating subplots
fig,axes = plt.subplots(1,5,figsize = (20,5)) 

#Plotting Line graphs
axes[0].plot(df['Months'],df['Sales'])
axes[0].set_title("Sales trend")
axes[0].set_xlabel("Months")
axes[0].set_ylabel("Sales")

#Bar chart
axes[1].bar(df['Months'],df['Sales'])
axes[1].set_title("Month wise Sales Comparision")
axes[1].set_xlabel("Months")
axes[1].set_ylabel("Sales")

#Pie chart
axes[2].pie(df['Sales'],labels = df['Months'])
axes[2].set_title("Contribution of each month")

#Histogram
axes[3].hist(df['Sales'],bins = 5, edgecolor = 'black')
axes[3].set_title("Frequency of Sales")

#Scatter Plot
axes[4].scatter(df.index, df['Sales'])
axes[4].set_title("Months Index vs Sales")

#displaying results
plt.show()
