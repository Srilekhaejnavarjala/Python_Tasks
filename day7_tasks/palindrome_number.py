""" Write a program to check whether a number is a Palindrome or not"""

def palindrome_num(num):
    s = 0
    original = num
    while num > 0:
        temp = num % 10
        num //= 10
        s = s * 10 + temp
    if original == s:
        print("Its a palindrome number")
    else:
        print("Its not a palindrome number")
palindrome_num(1221)


        
