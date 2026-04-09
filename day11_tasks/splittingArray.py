'''
14. Splitting Student Scores Across Servers
A dataset:
[50, 60, 70, 80, 90, 100, 110, 120]
Scenario:
A distributed system needs to divide this data among 4 servers.
Task:
● Convert to NumPy array.
● Split the array into 4 equal parts using array_split()
'''

#importing numpy
import numpy as np

#dataset
data = [50,60,70,80,90,100,110,120]

#converting into numpy
scores = np.array(data)
print(scores)

#splitting array into 4 rows
splitted_array = np.array_split(scores,4)
print(splitted_array)
