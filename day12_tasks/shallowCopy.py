'''
1. Student List Backup (Shallow Copy)
A teacher has a list of student marks:
marks = [50, 60, 70, 80]
Scenario:
She creates a backup using assignment:
backup = marks
Task:
● Modify the first element in marks.
● Observe the change in backup.
● Explain why both lists are affected.
'''

#importing numpy and copy modules
import numpy as np
import copy as c

#list of student marks
marks = [50,60,70,80]

#making it a numpy array
student_marks = np.array(marks)
backup = c.copy(student_marks)
backup[0] = 90
print("Original List: ",student_marks)
print("Backup List: ",backup)
