'''
5. Product Sales Bar Chart
Scenario:
products = ["Pen", "Book", "Pencil"]
sales = np.array([50, 80, 40])
Task:
● Create DataFrame
● Plot bar chart
● Add labels and title
'''

#importing modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#data
products = ["Pen", "Book", "Pencil"]
sales = np.array([50, 80, 40])

#creating data frame
df = pd.DataFrame({"Products":products ,"Sales":sales})
print(df)

#plot bar chart
plt.bar(df['Products'],height = df['Sales'],width = 0.8, align = "center")
plt.title("Product Sales Analysis")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()
