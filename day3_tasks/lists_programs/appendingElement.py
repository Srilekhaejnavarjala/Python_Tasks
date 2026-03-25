"""3. Write a program to add an element to a list using append()."""
li = [10,20,30,40,50]
print("The existing list elements: ",li)
n = input("enter element to insert: ")
ele = li.append(n)
print("Element inserted successfully.")
print("List after appending an element is: ",li)
