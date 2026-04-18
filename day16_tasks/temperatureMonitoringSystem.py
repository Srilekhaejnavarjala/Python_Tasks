'''
4. Temperature Monitoring System
Scenario:
temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
Task:
● Create DataFrame
● Plot:
○ Line graph → daily temperature trend
○ Bar chart → day-wise temperature
○ Pie chart → proportion of high (>30) vs low temps
○ Histogram → temperature frequency
○ Scatter plot → day index vs temperature
'''

#importing modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#data
temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

#creating DataFrame
df = pd.DataFrame({"Days": days, "Temperature": temps})

#categorizing high and low temperatures
df['Status'] = np.where(df['Temperature'] > 30, "High", "Low")

#creating subplots
fig, axes = plt.subplots(1, 5, figsize=(20,5))

#1. Line graph (trend)
axes[0].plot(df['Days'], df['Temperature'], marker='o')
axes[0].set_title("Daily Temperature Trend")
axes[0].set_xlabel("Days")
axes[0].set_ylabel("Temperature")

#2. Bar chart
axes[1].bar(df['Days'], df['Temperature'])
axes[1].set_title("Day-wise Temperature")
axes[1].set_xlabel("Days")
axes[1].set_ylabel("Temperature")

#3. Pie chart (High vs Low)
counts = df['Status'].value_counts()
axes[2].pie(counts, labels=counts.index, autopct='%1.1f%%')
axes[2].set_title("High vs Low Temperature")

#4. Histogram
axes[3].hist(df['Temperature'], bins=5, edgecolor='black')
axes[3].set_title("Temperature Distribution")
axes[3].set_xlabel("Temperature")
axes[3].set_ylabel("Frequency")

#5. Scatter plot
axes[4].scatter(df.index, df['Temperature'])
axes[4].set_title("Index vs Temperature")
axes[4].set_xlabel("Index")
axes[4].set_ylabel("Temperature")

#adjust layout
plt.tight_layout()

#show plots
plt.show()
