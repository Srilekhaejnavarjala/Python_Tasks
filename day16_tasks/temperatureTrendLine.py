'''
4. Temperature Trend Line Plot
Scenario:
Daily temperatures:
temps = np.array([28, 30, 32, 31, 29])
Task:
● Convert into Pandas Series
● Plot a line graph
● Add title and grid
'''

#importing modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#data
temps = np.array([28, 30, 32, 31, 29])

#converting into pandas series
series = pd.Series(temps)
print(series)

#Plotting line graph
plt.plot(series)
plt.title("Daily Temperature Trend")
plt.grid(visible = True)
plt.show()
