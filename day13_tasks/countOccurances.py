'''
7. Count Occurrences
You have:
data = np.array([1, 2, 2, 3, 1, 4, 2, 3])
Task:
● Count how many times each unique number appears.
● Return numbers with their counts.
'''

#importing numpy module
import numpy as np

#data
data = np.array([1, 2, 2, 3, 1, 4, 2, 3])
print(data)

#Count how many times each unique number appears
unique_nums = np.unique(data)
print("Unique numbers: ",unique_nums)

#Return numbers with their counts
for num in unique_nums:
    count = sum(data == num)
    print(f"{num}: {count}")
    

