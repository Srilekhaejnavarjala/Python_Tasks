'''
1. Monthly Sales Line Graph
Scenario:
A shop records monthly sales:
sales = np.array([100, 150, 200, 250, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May"]
Task:
● Convert data into a Pandas DataFrame
● Plot a line graph
● Label X-axis as months and Y-axis as sales
'''

#importing modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#data
sales = np.array([100, 150, 200, 250, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May"]

#converting data into data frame
df = pd.DataFrame({"Months": months, "Sales":sales})
print(df)

#Plot a line graph and labeling axis
plt.title("Monthly Sales Analysis")
plt.plot(df['Months'],df['Sales'])
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()


