'''
Splitting data for parallel processing
A dataset contains the following values:
[5, 10, 15, 20, 25, 30]
Scenario:
You want to distribute the data across 3 processors.
Task:
● Store the data in a NumPy array.
● Split it into 3 equal parts using NumPy.
'''

#importing numpy
import numpy as np

#dataset
data = [5,10,15,20,25,30]

#converting dataset into array
dataset = np.array(data)
print("The data is: ",dataset)

#splitting data into 3 parts
processors = np.array_split(dataset,3)
print("Array after splitting into 3 parts is: \n",processors)
