#Rectangle Area Calculator (Constructor)
'''
A geometry application needs to calculate the area of rectangles.
Create a Rectangle class that uses a constructor to initialize length and
width. Add a method to calculate and display the area.

'''

class Rectangle:
    def __init__(self):
        self.length = int(input("enter length of rectangle: "))
        self.width = int(input("enter width of rectangle: "))
        self.area_of_rectangle = self.length * self.width

    def display_area(self):
        print("The given length of rectangle is: ",self.length)
        print("The given width of rectangle is: ",self.width)
        print("The area of rectangle is: ",self.area_of_rectangle)

#creating object
r = Rectangle()

#displaying area of rectangle
r.display_area()


