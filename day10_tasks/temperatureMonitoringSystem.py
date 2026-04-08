'''
Temperature Monitoring System
A weather station records temperatures for two days.
Scenario:
Day 1: [30, 32, 31]
Day 2: [29, 33, 34]
Task:
● Create a 2D NumPy array to store this data.
● Print the array.
● Find the total temperature recorded.

'''

#imporing numpy
import numpy as np

#day 1 and day 2 temperature
day_1 = np.array([30,32,31])
day_2 = np.array([29,33,34])

#printing the recorded temperatures
print("The day 1 temperature is: ",day_1)
print("The day 2 temperature is: ",day_2)

#creating 2D array
temperature_of_two_days = np.array([day_1,day_2])
print("The type of the array is: ",temperature_of_two_days.ndim)

print(temperature_of_two_days)

#total temperature recorded
print("The sum of temperature recorded is: ",np.sum(temperature_of_two_days))

