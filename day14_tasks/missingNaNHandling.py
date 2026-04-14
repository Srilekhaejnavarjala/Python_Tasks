'''
2. Missing City Data (NaN Handling)
A dataset contains city populations:
cities = {"Delhi": 2000000, "Mumbai": 3000000, "Chennai": 1500000}
Scenario:
You want data for:
["Delhi", "Chennai", "Bangalore"]
Task:
● Create a Series with the above index
● Identify which cities have missing values (NaN)
'''

#importomg module
import pandas as pd

#city population dataset
cities = {"Delhi": 2000000, "Mumbai": 3000000, "Chennai": 1500000}
fetch_data = ["Delhi", "Chennai", "Bangalore"]

#creating panda series
population_data = pd.Series(cities, index = fetch_data)
print("City Population Data: ")
print(population_data)
print("----------------------------------------------------------------")


#Identifying which cities have missing values
nan_vals = population_data[population_data.isnull()].index
print(nan_vals)
print("----------------------------------------------------------------")
