'''
8. Pie Chart with Conditional Data
Scenario:
scores = np.array([40, 60, 80, 30, 90])
Task:
● Categorize into:
○ Pass (>50)
○ Fail (<=50)
● Count using NumPy/Pandas
● Plot pie chart for Pass vs Fail
'''

#importing modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#data
scores = np.array([40, 60, 80, 30, 90])

#categorizing scores
status = np.where(scores > 50,"Pass","Fail")

#converting to data frame
df = pd.DataFrame({"Scores":scores,"Status":status})
print(df)

#count Pass or Fail
counts = df['Status'].value_counts()
print(counts)

#plotting pie chart for Pass vs Fail
plt.pie(counts, labels = counts.index, autopct = '%1.1f%%')
plt.title("Pass vs Fail Distribution")
plt.show()

