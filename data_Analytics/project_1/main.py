#importing modules 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Reading dataset from csv file
data = pd.read_csv("C:/Users/Admin/Documents/pyCodes/data_Analytics/project_1/railway_gauges.csv")

#displaying first 5 and last 5 rows
print("First Five Rows: ")
print(data.head())
print("--------------------------------------------------------------------")

print("Last Five Rows")
print(data.tail())
print("--------------------------------------------------------------------")

#Finding out basic information
print(data.info())
print("--------------------------------------------------------------------")


#Statistical Information regarding dataset
print("Statistical Analysis: ")
print(data.describe())
print("--------------------------------------------------------------------")

#1. Finding in which year the gauge values are more ?
broad_gauge_max = data.loc[data['Broad Gauge'].idxmax(),'Year']
print(f"Broad Gauge Maximum value in year: {broad_gauge_max}")

narrow_gauge_max = data.loc[data['Narrow Gauge'].idxmax(),'Year']
print(f"Narrow Gauge Maximum value in year : {narrow_gauge_max}")

metre_gauge_max = data.loc[data['Metre Gauge'].idxmax(), 'Year']
print(f"Metre Gauge Maximum value in year: {metre_gauge_max}")
print("--------------------------------------------------------------------")

#2. Which gauge is having more demand overall?
broad_gauge = data['Broad Gauge'].sum()
narrow_gauge = data['Narrow Gauge'].sum()
metre_gauge = data['Metre Gauge'].sum()
print("Broad Gauge total usage in past years is: ",broad_gauge)
print("Narrow Gauge total usage in past years is: ",narrow_gauge)
print("Metre Gauge total usage in past years is: ",metre_gauge)
print("--------------------------------------------------------------------")

#Plotting them to view it visually
gauges = ["Broad Gauge","Narrow Gauge","Metre Gauge"]
values = [broad_gauge, narrow_gauge, metre_gauge]
plt.figure(figsize = (8,5))
plt.bar(gauges, values, color = 'orange')
plt.xlabel("Types of Gauges")
plt.ylabel("Respective Totals")
plt.title("Total Usage of Railway Gauges")
plt.show()

#3. Analysing the trends between gauge to gauge just by plotting them using
#years and those respective values
plt.figure(figsize = (10,6))
plt.plot(data['Year'],data['Broad Gauge'],marker = 'o',label = 'Broad Gauge')
plt.plot(data['Year'],data['Narrow Gauge'],marker = 'o',label = 'Narrow Gauge')
plt.plot(data['Year'],data['Metre Gauge'],marker = 'o',label = 'Metre Gauge')
plt.xlabel("Total Years")
plt.ylabel("Gauge Values")
plt.xticks(rotation = 70)
plt.title("Trend Analysis of Rail way Gauges")
plt.legend()
plt.grid()
plt.show()

#Finding out most used gauges
totals = data[['Broad Gauge','Metre Gauge','Narrow Gauge']].sum()
maximum_gauge = totals.idxmax()
print("Most Used Gauge in all the three are: ",maximum_gauge)
