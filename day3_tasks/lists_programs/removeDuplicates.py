"""7. Write a program to remove duplicate elements from a list."""
li = [10,20,10,20,30,40,50,60,40]
unique_elements = set(li)
print("The Original List: ",li)
print("The Unique element list: ",list(unique_elements))

"""
li = [10, 20, 20, 30, 40, 10, 50]
unique = []
for num in li:
    if num not in unique:
        unique.append(num)
print("After removing duplicates:", unique)
"""
