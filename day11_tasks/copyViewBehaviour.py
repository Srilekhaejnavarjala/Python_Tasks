'''
13. Copy vs View Behavior in Data Processing
Scenario:
A dataset:
[10, 20, 30, 40]
Task:
● Create a copy of the array.
● Modify the original array.
● Show that the copy does not change.
● Repeat using view() and observe the difference.
'''

#importing numpy
import numpy as np

#dataset
data1 = [10,20,30,40]
data2 = [60,70,80,90]

#creating a copy of array
dataset1 = np.array(data1)
dataset2 = np.array(data2)

copy_data = np.copy(dataset1)

new_data = np.append(dataset1,50)
print("Original dataset: ",new_data)
print("Copied dataset: ",copy_data)
print("--------------------------------------------")

#creating view of an array
dataset2 = np.append(dataset2,100)
view_data = dataset2.view()
print("Original dataset: ",dataset2)
print("View dataset: ",view_data)
