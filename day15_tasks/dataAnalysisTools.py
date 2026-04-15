'''
6. Data Analysis Tool (NumPy + Pandas)
Scenario:
Analyze student marks.
Task:
● Generate marks using NumPy
● Convert into Pandas DataFrame
● Use conditions to filter passing students
● Calculate mean using math/NumPy
● Use loop to print results
'''

#importing modules
import numpy as np
import pandas as pd

#generating marks using numpy
marks = np.random.randint(100,500,5)
print("Numpy Array: ")
print(marks)
print(type(marks))
print("------------------------------------------------------")

#converting into pandas dataframe
roll_nums = np.arange(1001,1006)
df = pd.DataFrame({"Roll_Nums": roll_nums, "Marks":marks})
print("Pandas Data Frame: ")
print(df)
print(type(df))
print("------------------------------------------------------")

#Use conditions to filter passing students
qualified_stu = df[df['Marks']>300]
print("Qualified Students: ")
print(qualified_stu)
print("------------------------------------------------------")

#Calculate mean using math/NumPy
average_marks = np.mean(df)
print("Average Marks scored by the students is: ")
print(average_marks)
print("------------------------------------------------------")

#Use loop to print results
looping_df = [df[i] for i in df]
print("Looping through Data Frame: ")
print(looping_df)
