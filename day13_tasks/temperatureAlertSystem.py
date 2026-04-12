'''
3. Temperature Alert System
Temperatures recorded in a city:
temps = np.array([28, 32, 35, 31, 29, 40, 38])
Task:
● Identify days where temperature is greater than 30.
● Return their indices.
'''

#importing numpy module
import numpy as np

#temperatures recorded in a city
temps = np.array([28,32,35,31,29,40,38])
print(temps)

#filtering temperatures greater than 30
filtered_temps = temps[temps > 30]
print(filtered_temps)
