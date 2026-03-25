"""4. Write a program to check whether an element exists in a tuple"""

tup = (10,21,23,45,32,67,43,31,89,78)
print("The elements in tuple are: ",tup)
ele = int(input("enter element to search: "))
for i in tup:
    if ele in tup:
        print(f"Element exists in tuple at {tup.index(ele)}")
        break
else:
    print("Element doesnt exist")
