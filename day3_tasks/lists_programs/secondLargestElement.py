"""8. Write a program to find the second largest number in a list."""
li = [65,10,20,21,21,12,32,1,56,78]
unique_list = set(li)
sorted_li = sorted(unique_list)
print("The list is: ",li)
print(sorted_li)
print("The second largest element in list is: ",sorted_li[-2])
