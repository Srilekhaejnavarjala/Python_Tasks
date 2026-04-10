'''
6. Multi-Level List Transformation (Advanced List Comprehension)
A dataset contains:
data = [[1, 2, 3], [4, 5], [6]]
Task:
● Flatten the list using list comprehension.
● Then create a new list containing squares of only even numbers.
'''

#nested list data
data = [[1,2,3],[4,5],[6]]
print("Original Data: ",data)

#flattening list using list comprehension
flattened_list = [a for d in data for a in d]
print("Flattened List: ",flattened_list)

#new list only with squares of even numbers
squared_list = [ num * num for num in flattened_list if num % 2 == 0]
print("Squared Even Number List: ",squared_list)
