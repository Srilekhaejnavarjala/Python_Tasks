'''
10. Data Cleaning + Visualization
Scenario:
data = np.array([100, np.nan, 200, 150, np.nan, 300])
Task:
1. Convert to Pandas Series
2. Replace NaN with mean
3. Plot:
○ Line graph of cleaned data
○ Bar chart of values > average
'''

#importing modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#data
data = np.array([100, np.nan, 200, 150, np.nan, 300])

#Convert to pandas series
series = pd.Series(data)
print(series)

#Replace NaN with mean
#Replace NaN with mean
average = series.mean()

updated_data = series.fillna(average)

#values > average
filtered_vals = updated_data[updated_data > average]

#plotting
fig, axes = plt.subplots(1, 2, figsize=(15,5))

#Line plot
axes[0].plot(updated_data)
axes[0].set_title("Cleaned Data")
axes[0].set_xlabel("Index")
axes[0].set_ylabel("Values")

#Bar plot 
axes[1].bar(filtered_vals.index, filtered_vals.values)
axes[1].set_title("Values > Average")
axes[1].set_xlabel("Index")
axes[1].set_ylabel("Values")

#displaying results
plt.show()

