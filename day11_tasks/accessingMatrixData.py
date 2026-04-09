'''
5. Accessing Matrix Data
A teacher stores marks of students in two subjects:
[[78, 85],
[90, 88],
[67, 72]]
Task:
● Convert it to a NumPy array.
● Access the second student's second subject mark.
'''

#importing numpy
import numpy as np

#marks of students in two subjects
stu_1 = [78,85]
stu_2 = [90,88]
stu_3 = [67,72]

#converting it to a 2D array
student_marks = np.array([stu_1,stu_2,stu_3])
print(student_marks)

#accessing second students second subject marks
print("Marks of third student who scored in subject 2 is: ")
print(student_marks[2,1])
