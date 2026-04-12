'''
2. Student Marks Analysis
Given marks of 5 students in 3 subjects:
marks = np.array([
[70, 80, 90],
[60, 75, 85],
[50, 65, 70],
[90, 95, 85],
[40, 55, 60]
])
Task:
● Calculate total marks of each student.
● Identify students whose total marks are above the class average
'''

#importing numpy module
import numpy as np

#student marks array
marks = np.array([
[70, 80, 90],
[60, 75, 85],
[50, 65, 70],
[90, 95, 85],
[40, 55, 60]
])
print("Marks of Students are: ",marks)

#calculating total marks of each student
total_marks = np.sum(marks,axis = 1)
print("Total marks of 5 students in 3 subjects is: ",total_marks)

#calculating average marks from total class
average_marks = np.mean(total_marks)
print("The Average Marks of the total marks scored by the student are: ")
print(average_marks)

#Identify students whose total marks are above the class average
filtered_marks = total_marks[total_marks > average_marks]
print("Students who scored more than class average are: ", filtered_marks)



