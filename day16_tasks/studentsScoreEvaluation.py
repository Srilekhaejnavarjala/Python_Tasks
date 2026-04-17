'''
2. Student Marks Bar Chart
Scenario:
Marks of students:
names = ["A", "B", "C", "D"]
marks = np.array([70, 85, 60, 90])
Task:
● Create a DataFrame
● Plot a bar graph
● Show student names on X-axis
'''

#importing modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#data
names = ["A", "B", "C", "D"]
marks = np.array([70, 85, 60, 90])

#creating a dataframe
df = pd.DataFrame({"Names":names, "Marks":marks})
print(df)

#plotting bar graph
plt.bar(df['Names'],height = df['Marks'], width = 0.8,align = "center")
plt.title("Score Evaluation")
plt.xlabel("Names")
plt.ylabel("Marks")
plt.show()
