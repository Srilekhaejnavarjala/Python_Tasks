"""5. Create a Number Guessing Game where:
● The program generates a random number between 1 and 50 using random.
● The user has 5 attempts to guess the number
● After each guess, calculate the absolute difference using math.fabs() and
display how far the guess is from the correct number."""
import random
import math
num = random.randint(1,50)
for i in range(5):
    guess = int(input("enter number between 1 to 50 to guess: "))
    if guess == num:
        print("You have guessed correctly!! Wohooo")
        break
    diff = math.fabs(num)-math.fabs(guess)
    print("The difference between actual number and guessed number is: ",diff)
else:
    print("Sorry the attempts met!! Try again")
    
    
