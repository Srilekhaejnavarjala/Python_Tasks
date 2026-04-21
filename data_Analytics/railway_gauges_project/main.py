'''
================================================================================================================
--------------------------------------Railway Gauges Data Analysis----------------------------------------------
----------------------Analyzing Railway Gauge Dataset using NumPy, Pandas and Matplotlib------------------------
================================================================================================================

================================================================================================================
#1. Importing Required Libraries
================================================================================================================
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
================================================================================================================
Scenario 1: Basic Data Loading & Cleaning
================================================================================================================
'''

#1.1 Load the dataset into a Pandas DataFrame.
data = pd.read_csv("C:/Users/Admin/Documents/pyCodes/data_Analytics/railway_gauges_project/railway_gauges.csv")
print("railway_gauges.csv.")
print("-----------------------------------------------------------------")

#1.2. Display the first 5 rows and column names.
print("Displaying first 5 rows of the dataset: ")
print(data.head())
print("-----------------------------------------------------------------")

#1.3. Check for missing values and replace them with 0.
print("Checking for missing values and filling them: ")
updated_data = data.fillna(0)
#fillna() is used to fill the null values or NaN values existing in the dataset

print("Updated dataset is: ")
print(updated_data)
print("-----------------------------------------------------------------")

#1.4. Convert all gauge columns (Broad, Metre, Narrow, Total) to Numeric type
updated_data['Year'] = updated_data['Year'].astype(str).str.split('-').str[0].astype(int)
updated_data[['Broad Gauge','Metre Gauge','Narrow Gauge','Total']] = updated_data[['Broad Gauge','Metre Gauge','Narrow Gauge','Total']].astype(int)
print("Converted them into Numeric Type")
print("-----------------------------------------------------------------")


'''
================================================================================================================
Scenario 2: Simple Visualization
================================================================================================================
'''

#2.1. Extract Year and Total columns
df = updated_data[["Year","Total"]]
print(df)

#2.2. Plot a line graph showing Total Tracks over years
plt.plot(df['Year'], df['Total'])
plt.title("Total Tracks Over Years")
plt.xlabel("Years")
plt.ylabel("Total Tracks")
plt.xticks(rotation=60)
plt.tight_layout()
plt.show()
print("-----------------------------------------------------------------")


'''
================================================================================================================
Scenario 3: Filtering + Bar Chart
================================================================================================================
'''

#3.1. Filter the dataset for years after 2000.
filtered_df = updated_data[updated_data['Year'] > 2000]
print(filtered_df)
print("-----------------------------------------------------------------")

#3.2 Select Broad Gauge, Metre Gauge and Narrow Gauge
dataset = filtered_df[["Year", "Broad Gauge", "Metre Gauge", "Narrow Gauge"]]

#3.3 Plot a grouped bar chart comparing all three gauges
dataset.set_index('Year').plot(kind='bar', figsize=(12, 6))
plt.title("Gauge Comparison After 2000")
plt.xlabel("Years")
plt.ylabel("Count")
plt.xticks(rotation=45)

#3.4 Adding legend and proper labels
plt.legend(title='Gauge Type')
plt.tight_layout()
plt.show()

#3.5 Calculate total for each gauge
totals = dataset[['Broad Gauge', 'Metre Gauge', 'Narrow Gauge']].sum()
print("Total: ", totals)
#Finding dominant gauge in recent years
high = totals.idxmax()
print(f"Most demanded Gauge in recent years: {high}")


'''
================================================================================================================
Scenario 4: Feature Engineering + Pie Chart
================================================================================================================
'''

#4.1. Calculate total sum of each gauge across all years

total_sum = updated_data[['Broad Gauge', 'Metre Gauge', 'Narrow Gauge']].sum()
print("Total sum of each gauge across all years is : ", total_sum)

#4.2 Create a new structure (Series/DF) for totals

summed_df = pd.Series(total_sum, name='Gauge_Totals')
print(summed_df)

#4.3 Plot a pie chart showing percentage contribution
plt.pie(summed_df, labels=summed_df.index, autopct='%1.1f%%')
plt.title("Gauge Distribution for Years")

#4.4 Add Percentage labels (autopct)
plt.legend(title="Gauge Type")
plt.tight_layout()
plt.show()


'''
================================================================================================================
Scenario 5: Advanced Analysis + Multiple Graphs
================================================================================================================
'''

#5.1 Create new Columns (Broad_Gauge%, Narrow_Gauge%, Metre_Gauge%)
updated_data['Broad_Gauge%'] = (updated_data['Broad Gauge'] / updated_data['Total']) * 100
updated_data['Metre_Gauge%'] = (updated_data['Metre Gauge'] / updated_data['Total']) * 100
updated_data['Narrow_Gauge%'] = (updated_data['Narrow Gauge'] / updated_data['Total']) * 100

#5.2 Use NumPy (np.diff) to calculate yearly growth of Total Tracks
diff = np.diff(updated_data['Total'])
prev_year_vals = updated_data['Total'].iloc[:-1].values
growth = (diff / prev_year_vals) * 100

updated_data['Yearly_Growth(in %)'] = np.insert(growth, 0, 0)

#5.3 Plot Line graph for all gauges and Stacked Bar chart showing comparison
plt.figure(figsize=(10, 5))
plt.plot(updated_data['Year'], updated_data['Broad Gauge'], label='Broad Gauge')
plt.plot(updated_data['Year'], updated_data['Metre Gauge'], label='Metre Gauge')
plt.plot(updated_data['Year'], updated_data['Narrow Gauge'], label='Narrow Gauge')

plt.title("Gauge Trends")
plt.xlabel("Year")
plt.ylabel("Count")
plt.legend()
plt.xticks(rotation=60)
plt.tight_layout()
plt.show()

updated_data.set_index('Year')[['Broad Gauge', 'Metre Gauge', 'Narrow Gauge']].plot(
    kind='bar', stacked=True, figsize=(12, 6)
)
plt.title("Gauge Composition Over Years")
plt.xlabel("Year")
plt.ylabel("Total Tracks")
plt.xticks(rotation=45)
plt.legend(title="Gauge Type")
plt.tight_layout()
plt.show()

#5.4 Highlight years with highest growth and Decline in any gauge

max_growth = updated_data['Yearly_Growth(in %)'].max()
year_max_growth = updated_data.loc[
    updated_data['Yearly_Growth(in %)'] == max_growth, 'Year'
].values[0]

print(f"Highest growth observed in {year_max_growth} with {max_growth:.2f}%")

decline = updated_data[
    (updated_data['Broad Gauge'].diff() < 0) |
    (updated_data['Metre Gauge'].diff() < 0) |
    (updated_data['Narrow Gauge'].diff() < 0)
]

print("Years with decline in any gauge:")
print(decline[['Year', 'Broad Gauge', 'Metre Gauge', 'Narrow Gauge']])


'''
================================================================================================================
-----------------------------------------------------THE END----------------------------------------------------
================================================================================================================
'''
