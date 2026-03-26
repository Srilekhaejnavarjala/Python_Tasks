"""2. Write a program to find the length of a list."""
n = int(input("enter size of the list: "))
li = []
for i in range(n):
    ele = int(input("enter element to insert: "))
    li.append(ele)
print("The elements in the list are: ",li)
print("The length of the list is: ",len(li))
