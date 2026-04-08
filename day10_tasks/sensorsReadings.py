'''

4. Combine Two Sensor Readings
Two sensors record readings during a test.
Scenario:
Sensor1 = [10, 20, 30]
Sensor2 = [40, 50, 60]
Task:
● Store both readings in NumPy arrays.
● Combine them into one array using NumPy concatenation.

'''

#import numpy
import numpy as np

#sensor recordings
sensor_1 = [10,20,30]
sensor_2 = [40,50,60]

#converting it into numpy arrays
data_1 = np.array(sensor_1)
data_2 = np.array(sensor_2)
print("Sensor 1: ",data_1)
print("Sensor 2: ",data_2)

#combining sensors data into one using concatenation
sensors_data = np.concatenate((data_1,data_2))
print("Sensors data after concatenation is: ",sensors_data)
