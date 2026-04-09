'''
10. Find Indexes of Specific Value
A quality check system stores product defect codes:
[2, 4, 1, 4, 3, 4, 5]
Task:
● Find the indexes where value = 4 using NumPy searching.
'''

#importing numpy
import numpy as np

#product defect codes
product_codes = [2,4,1,4,3,4,5]

#converting data into numpy array
defect_codes = np.array(product_codes)
print(defect_codes)

#Finding the value using indexing
search_value = np.searchsorted(defect_codes, 4)
print("The index of defect code 4 is: ",search_value)
print("The indexes of defect code in the given list is: ",np.where(defect_codes == 4))
