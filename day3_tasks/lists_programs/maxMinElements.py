"""5. Write a program to find the largest and smallest element in a list."""
li = [10,12,8,30,40,56,19]
print("Elements existing in the list are: ",li)
maximum_element = max(li)
minimum_element = min(li)
print("The maximum element in the list is: ",maximum_element)
print("The minimum element in the list is: ",minimum_element)
print("---------------------------------------------------------------\n")
sorted_list = sorted(li)
print("The minimum element: ",sorted_list[0])
print("The maximum element: ",sorted_list[-1])
