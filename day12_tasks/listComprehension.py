'''
2. Even Number Filter (List Comprehension)
A system stores numbers:
nums = [1, 2, 3, 4, 5, 6]
Task:
● Use list comprehension to create a new list containing only even numbers.
'''

#Implementing list comprehension
#system data
nums = [1,2,3,4,5,6]
print("The elements in the list are: ")
print(nums)

#new list only with even nums
new_nums = [num for num in nums if num % 2 == 0]
print("New list with even numbers only: ")
print(new_nums)
