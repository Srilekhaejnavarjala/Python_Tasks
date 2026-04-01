#Student Result Generator (Method overloading concept)
'''
A school system calculates student results differently depending on
available data. Create a Result class where a method can calculate the
result using either two subjects or three subjects.

'''
class Result:
    
    def data(self):
        self.name = input("Enter student name: ")
        n = int(input("Enter number of subjects: "))
        
        self.student_marks = []
        
        for i in range(n):
            mark = int(input(f"Enter subject {i+1} marks: "))
            self.student_marks.append(mark)

    # Overloading using *args
    def calculate_marks(self, *marks):
        total = sum(marks)
        print(f"Total marks of {self.name} is: {total}")


# object
res = Result()

res.data()

# direct call (no if-else needed)
res.calculate_marks(*res.student_marks)

        
