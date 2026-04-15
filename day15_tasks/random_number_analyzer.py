'''
2. Random Number Analyzer
Scenario:
A system generates random numbers for testing.
Task:
● Use random to generate 10 numbers
● Store in a list
● Use loop + condition to count even/odd numbers
● Use set to remove duplicates
'''

#importing modules
import random 

#defining function
def random_number_analyzer():

    #creating a list which stores 10 values
    nums = [random.randint(1,100) for i in range(10)]
    random_nums = list(nums)
    print("Random Numbers list is: ")
    print(random_nums)
    print("-------------------------------------------")

    #Use Loop + Condition to count even, odd numbers
    even_nums = []
    odd_nums = []
    for i in random_nums:
        if i % 2 == 0:
            even_nums.append(i)
        else:
            odd_nums.append(i)
    print("Even number list: ")
    print(even_nums)
    print("Total number of evens are: ",len(even_nums))

    print("Odd number list: ")
    print(odd_nums)
    print("Total number of odds are: ",len(odd_nums))
    print("-------------------------------------------")

    #Use set to remove duplicates
    unique_list = list(set(random_nums))
    print("Unique List after removing duplicates are: ")
    print(unique_list)
random_number_analyzer()

