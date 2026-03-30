"""Write a program to check whether a given number is an Armstrong number
or not."""
def armstrong_number(num):
    s = 0
    original = num
    while num>0:
        temp = num%10
        num //= 10
        s += pow(temp,3)
    print(s)
    if original == s:
        print("It is an Armstrong number")
    else:
        print("It is not an Armstrong number")
armstrong_number(153)
