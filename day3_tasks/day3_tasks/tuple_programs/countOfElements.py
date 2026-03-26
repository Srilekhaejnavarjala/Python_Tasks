"""5. Write a program to count how many times an element
appears in a tuple"""
tup = (12,32,34,32,56,76,34,67,87,23,23,66,55,88,34)
print("The tuple is: ",tup)
ele = int(input("enter element to count: "))
rep = tup.count(ele)
print(f"Elements count in tuple is: {rep} ")
