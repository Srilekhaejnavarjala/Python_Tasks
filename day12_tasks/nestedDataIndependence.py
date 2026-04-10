'''
5. Nested Data Independence (Deep Copy)
A school stores classroom data:
classes = [["Math", [30, 35]], ["Science", [25, 28]]]
Scenario:
● Create a deep copy of this structure.
● Modify student count in original.
Task:
● Prove that copied data remains unchanged.
● Explain why deep copy is required here
'''

#importing copy module
import copy as c

#classroom data
classes = [["Math", [30, 35]], ["Science", [25, 28]]]
print("-------Before Deep Copy-------")
print(classes)

#deepcopy of list
deepcopy_classes = c.deepcopy(classes)
classes[0][1][0] = 45
classes[1][1][1] = 68
print("-------After Deep Copy-------")
print("Original List: ",classes)
print("Copied List: ",deepcopy_classes)
