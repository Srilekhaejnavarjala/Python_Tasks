'''
3. Expense Distribution Pie Chart
Scenario:
Monthly expenses:
expenses = np.array([500, 300, 200])
labels = ["Food", "Rent", "Travel"]
Task:
● Create a pie chart
● Show percentage distribution
'''

#importing modules
import numpy as np
import matplotlib.pyplot as plt

#data
expenses = np.array([500, 300, 200])
label = ["Food", "Rent", "Travel"]
my_explode = [0.1,0,0]

#creating a pie chart
plt.pie(expenses, labels = label,explode = my_explode, autopct = '%1.0f%%')
plt.title("Expense Distribution")
plt.axis('equal')
plt.show()
