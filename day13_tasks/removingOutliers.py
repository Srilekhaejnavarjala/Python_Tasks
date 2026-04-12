'''
6. Remove Outliers
Given data:
values = np.array([10, 12, 15, 18, 100, 14, 13])
Task:
● Compute the mean and standard deviation
● Remove values that are more than 2 standard deviations from the mean
'''

#importing numpy module
import numpy as np

#data
values = np.array([10,12,15,18,100,14,13])
print("Values: ",values)

#compute mean and standard deviation
mean_values = np.mean(values)
standard_deviation = np.std(values)
print("Mean: ",mean_values)
print("Standard Deviation: ",standard_deviation)

#defining limits
lower_limit = mean_values - 2 * standard_deviation
upper_limit = mean_values + 2 * standard_deviation

#filtering data
filtered_values = values[(values < lower_limit) & (values > upper_limit)]
print("The list is empty as there are no outliers",filtered_values)

