'''
Data Processing Pipeline
A data pipeline receives the following array:
[12, 7, 25, 3, 18, 10]
Scenario:
1. Convert the list into a NumPy array.
2. Sort the array.
3. Split the sorted array into two equal parts.
4. Calculate the sum of each part.
Output:
● Sorted array
● Two split arrays
● Sum of each part
'''

#importing numpy
import numpy as np

#data
data = [12,7,25,3,18,10]

#converting list to array
new_data = np.array(data)
print("The data is: ",new_data)

#sorting data
sorted_data = np.sort(new_data)
print("Sorted data is: ",sorted_data)

#splitting sorted data into 2
splitted_data = np.array_split(sorted_data,2)
print("The splitted arrays are: ",splitted_data)

#calculate the sum of each part
for sub in splitted_data:
    print(f"The sum of section {sub} is: ",np.sum(sub))

