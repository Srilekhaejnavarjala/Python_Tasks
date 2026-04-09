'''
11. Filter High Temperature Values
A weather station records temperatures:
[28, 31, 35, 27, 40, 22]
Scenario:
The system needs temperatures above 30°C.
Task:
● Filter the values greater than 30 using NumPy boolean filtering.
'''

#importing numpy
import numpy as np

#weather station records
weather_records = [28,31,35,27,40,22]

#converting it to an array
temp_records = np.array(weather_records)
print(temp_records)

#filtering values greater than 30 degrees
high_temps = temp_records[temp_records > 30]
print("Temperature greater than 30 degrees is: \n",high_temps)
