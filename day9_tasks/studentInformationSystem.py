#Student Information System
'''
A school wants a program to store student details. Create a Student class
with attributes such as name, roll number, and marks. Create objects for
at least three students and display their details.

'''

class Student_Details:
    
    def __init__(self,name,roll_number,marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
        
    def display_details(self):
        print("Name: ",self.name)
        print("Roll Number: ",self.roll_number)
        print("Marks: ",self.marks)
        print()

print("Student Details are: \n")

#creating objects       
student_1 = Student_Details("Abhimanyu","1001",98)
student_2 = Student_Details("Bheeshma","1002",96)
student_3 = Student_Details("Nakul","1003",90)
student_4 = Student_Details("Sahadev","1004",92)

#displaying details
student_1.display_details()
student_2.display_details()
student_3.display_details()
student_4.display_details()
