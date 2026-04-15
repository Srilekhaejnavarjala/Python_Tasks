'''
10. Advanced Simulation System
Scenario:
Simulate exam results and generate reports.
Task:
● Generate random marks using random
● Store in NumPy array
● Convert to Pandas DataFrame
● Use OOP to represent Student
● Use conditions + loops to assign grades
● Save report to file
● Handle errors using try-except
● Use math module for statistics
'''
#importing modules
import numpy as np
import pandas as pd
import math
import random

try:
    #generating random marks using random
    marks = [random.randint(100,600) for i in range(5)]

    #storing marks in numpy array
    marks_arr = np.array(marks)
    print("Numpy Array: ")
    print(marks_arr)
    print(type(marks_arr))

    #Converting into pandas data frame
    roll_nums = np.arange(1001,1006)
    df = pd.DataFrame({"Roll_Nums": roll_nums, "Marks": marks_arr})
    print("\nStudent Marks Sheet: ")
    print(df)

    #Use OOPs to represent students
    class Student:
        def __init__(self, name, marks):
            self.name = name
            self.marks = marks
            self.grade = None
        
        def assign_grade(self):
            if self.marks >= 500:
                self.grade = "A"
            elif self.marks >= 400:
                self.grade = "B"
            elif self.marks >= 300:
                self.grade = "C"
            else:
                self.grade = "D"

    students = []

    #creating objects
    for i in range(len(marks)):
        s = Student(f"Stu_{i+1}", marks[i])
        s.assign_grade()
        students.append(s)

    print("\nStudent Results:")
    for s in students:
        print(s.name, s.marks, s.grade)

    #Using math module for statistics
    total = sum(marks)
    average_marks = math.floor(total / len(marks))   # using math
    max_marks = max(marks)
    min_marks = min(marks)

    print(f"\nAverage marks: {average_marks}")
    print(f"Maximum marks: {max_marks}")
    print(f"Minimum marks: {min_marks}")

    #Saving report to the file
    with open("student_report.txt", "w") as f:
        f.write("Student Report\n")
        f.write("------------------------\n")

        for s in students:
            f.write(f"{s.name} | Marks: {s.marks} | Grade: {s.grade}\n")

        f.write("\nStatistics:\n")
        f.write(f"Average: {average_marks}\n")
        f.write(f"Max: {max_marks}\n")
        f.write(f"Min: {min_marks}\n")

    print("\nReport saved successfully in 'student_report.txt'")

except Exception as e:
    print("Error occurred:", e)
    
            
            
