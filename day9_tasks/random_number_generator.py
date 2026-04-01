#Random Number Generator (Generators)
'''
A program is needed to generate numbers for testing purposes.
Create a generator function that produces numbers from 1 to N and
prints them one by one when iterated.
'''

import random
def number_generator():
    num = int(input("enter how many random numbers: "))
    for i in range(num):
        nums = random.randint(1,100)
        yield nums

#displaying results
for value in number_generator():
    print(value, end = " ")
