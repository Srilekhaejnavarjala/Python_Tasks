#Shape Area Calculator
'''
A graphics application needs to calculate the area of different shapes.
Create classes Circle, Rectangle, and Triangle, each having an area() method. Demonstrate
polymorphism by calling the same method for different objects.

'''

class Circle:
    def area(self):
        radius = 4
        pi = 3.14
        area = pi * (radius ** 2)
        print(f"The radius is {radius}")
        print(f"The area of circle is: {area}")
        print("---------------------------------------------\n")
        
class Rectangle:
    def area(self):
        length = 10
        width = 50
        area = length * width
        print(f"The given length is {length}")
        print(f"The given width is {width}")
        print(f"The area of rectangle is: {area}")
        print("---------------------------------------------\n")
        
class Triangle:
    def area(self):
        base = 43
        height = 180
        area = 0.5 * base * height
        print(f"The given base is {base}")
        print(f"The height given is {height}")
        print(f"The area of triangle is: {area}")
        print("---------------------------------------------\n")

#creating object
c = Circle()
r = Rectangle()
t = Triangle()

#displaying results
c.area()
r.area()
t.area()

    
    
        
