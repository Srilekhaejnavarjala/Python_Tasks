'''

1. Student Marks Analysis
A teacher stores the marks of 5 students in a NumPy array.
Scenario:
You are given marks [45, 67, 89, 56, 72].
Task:
● Convert the list into a NumPy array.
● Add 5 grace marks to every student.
● Print the updated marks.

'''

#importing numpy package
import numpy as np

#creating a numpy array using lists
scores = [45,67,89,56,72]
print("The type of scores is: ",type(scores))
student_marks = np.array(scores)
print("The type of student_marks is: ",type(student_marks))
print("\n----------------------------------------------------------")
print("The student scores BEFORE adding grace marks is:  ")
print(student_marks)
print("\n-----------------------------------------------------------")

#adding grace marks of 5
updated_marks = np.array(student_marks + 5)
print("The student scores AFTER adding grace marks is: ")
print(updated_marks)

