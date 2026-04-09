'''
4. Student Roll Numbers Extraction
A list contains roll numbers:
[101, 102, 103, 104, 105, 106]
Scenario:
You want only the middle students (index 2 to 4).
Task:
● Use NumPy slicing to extract those values.
'''

#importing numpy
import numpy as np

#roll numbers
roll_nums = [101,102,103,104,105,106]

#converting into numpy array
stu_roll_nums = np.array(roll_nums)
print(stu_roll_nums)

#only middle students from 2 to 4th index
print("Students from second index to fourth index are: ")
print(stu_roll_nums[2:5])

