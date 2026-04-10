'''
3. Employee Data Copy Issue (Shallow vs Deep Copy)
A company stores employee data:
employees = [[101, "A"], [102, "B"], [103, "C"]]
Scenario:
● Create a shallow copy of the list.
● Modify one nested list (e.g., change "A" to "Z").
● Observe changes in both lists.
Task:
● Explain why the change reflects in both.
● Fix it using deep copy.
'''
#importing copy module
import copy as c

# employee data
employees = [[101,"A"],[102,"B"],[103,"C"]]

# shallow copy
data = c.copy(employees)
data[0][1] = "Z"

print("After Shallow Copy:")
print("Original List: ", employees)
print("Copied List: ", data)

# reset original data
employees = [[101,"A"],[102,"B"],[103,"C"]]

# deep copy
deep_data = c.deepcopy(employees)
deep_data[0][1] = "Z"

print("\nAfter Deep Copy:")
print("Original List: ", employees)
print("Deep Copied List: ", deep_data)

