'''
8. Random Data & Filtering
Generate random numbers:
nums = np.random.randint(1, 100, 10)
Task:
● Filter values that are divisible by 5
● Return sorted result
'''

#importing numpy module
import numpy as np

#generate random numbers
nums = np.random.randint(1,100,10)
print("Numbers Array: ",nums)

#Filter values that are divisible by 5
divisible_nums = nums[nums % 5 == 0]
print("Divisible Numbers Array: ",divisible_nums)

#Return sorted results
sorted_nums = np.sort(divisible_nums)
print("Sorted Array: ",sorted_nums)
