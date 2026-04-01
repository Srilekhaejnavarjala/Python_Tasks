#Vehicle Management System
'''
A transport company manages different vehicles. Create a base class Vehicle
with attributes like brand and speed. Create derived classes Car and Bike
that inherit from Vehicle and display their details.
'''
class Vehicle:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
        
class Car(Vehicle):
    
    def display_details(self):
        print("Its car class!!")
        print("Brand Name: ",self.brand)
        print("Speed per kilometer: ",self.speed)
        
class Bike(Vehicle):

    def display_details(self):
        print("Its bike class!!")
        print("Brand Name: ",self.brand)
        print("Speed per kilometer: ",self.speed)

#creating objects
car = Car("BMW",305)
bike = Bike("Royal Enfield",220)

#displaying results
car.display_details()
bike.display_details()

    
        
    
    
