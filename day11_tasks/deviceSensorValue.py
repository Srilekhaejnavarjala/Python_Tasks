'''
2. Device Sensor Value (Scalar Array)
An IoT device records a single sensor reading = 75.
Task:
● Create a 0-D NumPy array with this value.
● Print the value and check its number of dimensions.
'''

#importing numpy
import numpy as np

#taking inputs
sensor_value = int(input("enter number to store: "))

#making it an array
iot_sensor = np.array(sensor_value)
print("The recorded sensor value is: ",iot_sensor)

#printing its number of dimensions
print("The array is : ",type(iot_sensor),"and its dimension is: ",iot_sensor.ndim)



