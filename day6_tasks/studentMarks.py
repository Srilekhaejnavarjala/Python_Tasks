"""

Develop a Python program to manage student marks for three subjects.
Store the subject names in a tuple, maintain unique student
names in a set, and store each student’s marks
in a list inside a dictionary where the key is the student name.

Create user-defined
functions to add a student with marks, display all student records,
and calculate the average marks of a student.

Implement a recursive function to calculate the total marks from the list of
marks. The program should interact with the user through a simple menu.
Also include exception handling to handle ValueError
(non-numeric marks input), ZeroDivisionError
(average calculation issues), TypeError (incorrect data type in marks),
and NameError (when a student name entered does not exist in the dictionary)

"""
def total_marks(marks_list):
    # Recursive function to calculate total
    if len(marks_list) == 0:
        return 0
    return marks_list[0] + total_marks(marks_list[1:])


def student_subjects():
    tup = ("Math", "Science", "English")
    stu_data = dict()
    student_names = set()

    while True:
        try:
            print("\n1. Add student")
            print("2. Display Records")
            print("3. Calculate Average")
            print("4. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                name = input("Enter student name: ")
                student_names.add(name)

                marks_list = []
                for subject in tup:
                    marks = int(input(f"Enter marks for {subject}: "))
                    marks_list.append(marks)

                stu_data[name] = marks_list   

            elif choice == 2:
                print("\nStudent Records:")
                for name, marks in stu_data.items():   
                    print(name, "=", marks)

            elif choice == 3:
                name = input("Enter student name: ")   

                if name not in stu_data:
                    raise NameError

                marks_list = stu_data[name]

                total = total_marks(marks_list)
                avg = total / len(marks_list)

                print(f"Total Marks: {total}")
                print(f"Average Marks: {avg}")

            elif choice == 4:
                break

            else:
                print("Invalid choice")

        except ValueError:
            print("Please enter numeric values only!!")

        except ZeroDivisionError:
            print("Cannot calculate average (no marks)")

        except TypeError:
            print("Invalid data type in marks!")

        except NameError:
            print("Student not found")

    print("\nFinal Data:", stu_data)


student_subjects()
