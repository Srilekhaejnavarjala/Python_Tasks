"""Write a program to check whether a number is a perfect number"""

def perfect_num(num):

    original = num
    temp = []
    if num <= 1:
        print("No divisors to check number as it is less than 1")
    else:
        for i in range(1,original):
            if original % i == 0:
                temp.append(i)
        if original == sum(temp):
            print("It is a perfect number")
        else:
            print("Its not a perfect number")
perfect_num(6)
