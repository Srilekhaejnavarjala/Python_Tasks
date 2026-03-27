"""Write a Python program that generates 20 random numbers between
1 and 200 using the random module and store them in a list.
Then using the math module, compute and display:
● Maximum value
● Minimum value
● Square root of the maximum number
● Logarithm of the minimum number"""

import random
import math
numbers = []
for i in range(20):
    num = random.randint(1,200)
    numbers.append(num)
print(numbers)
max_number = max(numbers)
min_number = min(numbers)
square_root_max = math.sqrt(max_number)
log_min = math.log(min_number)
print("The maximum value of the given list is: ",max_number)
print("The minimum value of the given list is: ",min_number)
print("The square root of the maximum number is: ",square_root_max)
print("The logarithm of the minimum number is: ",log_min)
