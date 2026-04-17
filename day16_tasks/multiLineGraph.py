'''
6. Multi-Line Graph for Sales Comparison
Scenario:
data = {
"Month": ["Jan", "Feb", "Mar"],
"Store_A": [100, 150, 200],
"Store_B": [90, 140, 210]
}
Task:
● Create DataFrame
● Plot two line graphs on same plot
● Add legend
'''

#importing modules
import pandas as pd
import matplotlib.pyplot as plt

#data
data = {
"Month": ["Jan", "Feb", "Mar"],
"Store_A": [100, 150, 200],
"Store_B": [90, 140, 210]
}

#creating data frame
df = pd.DataFrame(data)
print(df)

#Plot two line graphs on same plot
plt.plot(df['Month'],df['Store_A'], label = "Store A")
plt.plot(df['Month'],df['Store_B'], label = "Store B")
plt.xlabel("Month")
plt.ylabel("Stores")
plt.title("Sales Comparision")
plt.legend()
plt.show()
