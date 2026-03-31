"""1. Student Attendance Record"""
'''A teacher wants to store student attendance in a file named
attendance.txt.
Write a Python program that takes a student name as input and
appends it to the file. Then display the contents of the file.'''


def student_attendance_record():
    try:
        students = []
        attendance_file = open("attendance.txt",'w')
        n = int(input("enter number of students : "))

        #Appending student names to the text file
        for i in range(1,n+1):
            student_names = input(f"enter student {i} name: ")
            attendance_file.write(f"{i}. {student_names}\n")
            
        attendance_file.close()
        
        print("Student names are: ",attendance_file)
        print("Student names appended successfully.")


        #Display file content
        attendance_file = open("attendance.txt",'r')
        print("The Students Attendance List: ")
        print(attendance_file.read())
        attendance_file.close()

        #If try block meets error, It goes to except 
    except ValueError or TypeError:
        print("Enter only strings to store")
    
student_attendance_record()
