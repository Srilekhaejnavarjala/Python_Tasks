'''
1. Student Score Processor
Scenario:
A teacher stores student names and marks in a list of tuples.
Task:
● Convert data into a dictionary
● Use a loop + condition to find students scoring above 50
● Use math module to calculate average
● Store results in a text file
'''

#importing module
import math as m

#defining a function
def student_score_processor():
    #creating user input values
    names = []
    marks = []
    student_details = {}
    n = int(input("enter number of  students to be added: "))
    for i in range(n):
        name = input(f"enter student {i+1} name: ")
        mark = int(input(f"enter marks for student {i+1}: "))
        names.append(name)
        marks.append(mark)

    #converting into dictionary
    student_details = dict(zip(names,marks))
    print(student_details)

    #Use a loop + condition to find students scoring above 50
    highest_score = {}
    for key,value in student_details.items():
        if value > 50:
            highest_score[key] = value
    print("The highest marks scored by the students are: ",highest_score)

    #Use math module to calculate average
    average_marks = sum(student_details.values())/len(student_details)
    print("The Average Marks obtained by the students is: ",average_marks)
            
    #Store results in a text file
    user = input("Do you wanna store it in text file? (Y/N)  ")
    if user.lower() == 'y':
        with open("dictionary_data",'w') as txt:
            txt.write("Student Details: \n")
            txt.write(str(student_details)+"\n")

            txt.write("Students scoring above 50 are: \n")
            txt.write(str(highest_score)+"\n")

            txt.write("Average Marks: \n")
            txt.write(str(average_marks)+"\n")
            
        print("Successfully stored data in a text file.")
    else:
        print("Sorry! I cannot store the results in txt file!! TRY AGAIN")
student_score_processor()

        
