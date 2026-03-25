"""6. Write a program to reverse a list."""
n = int(input("enter size of list: "))
li = []
for i in range(n):
    ele = int(input("enter element to insert: "))
    li.append(ele)
print("The list before reversing is: ",li)
print("The reverse of a list is: ",li[::-1])
