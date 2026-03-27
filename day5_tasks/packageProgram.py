"""A company wants to organize its Python code using packages.
Create a package named utilities that contains two modules:
● math_operations.py (functions for addition and multiplication)
● string_operations.py (functions to convert string to uppercase and count
characters)
Write a Python program that imports the package and uses functions
from both modules"""

from utilities import math_operations
from utilities import string_operations

#Math_operations
print("Addition: ",math_operations.add(10,5))
print("Subtraction: ",math_operations.subtract(100,5))
print("Multiply: ",math_operations.multiply(10,50))
print("Division: ",math_operations.divide(10,5))

#string_operations
s = input("enter string: ")
print("Uppercase: ",string_operations.to_upper(s))
print("Lowercase: ",string_operations.to_lower(s))
print("Camelcase: ",string_operations.to_capitalize(s))
print("Swapcase: ",string_operations.to_swapcase(s))


