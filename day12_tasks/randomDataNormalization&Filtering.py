'''
12. Random Dataset Normalization + Filtering
Scenario:
● Generate 8 random float values between 0 and 1.
Task:
1. Normalize by multiplying with 100
2. Filter values greater than 50
3. Sort the filtered values
'''

#importing numpy
import numpy as np

#generating random numbers between 0 and 1
numbers = np.random.random(size = 8)
rounded_nums = np.round(numbers,2) 
print(rounded_nums)

#normalizing by multiplying with 100
normalized_nums = rounded_nums * 100
print("Normalized Numbers: ",normalized_nums)

#filter values greater than 50
filtered_values = normalized_nums[normalized_nums > 50]
print("Filtered Numbers: ",filtered_values)

#Sorting filtered values
sorted_nums = np.sort(filtered_values)
print("Sorted Numbers: ",sorted_nums)


