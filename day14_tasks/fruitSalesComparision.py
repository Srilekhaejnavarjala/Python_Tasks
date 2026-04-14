'''
11. Fruit Sales Comparision (Series Addition)
A shop tracks fruit sales:
S1 = pd.Series([10, 20, 30], index=["apple", "banana", "cherry"])
S2 = pd.Series([5, 15, 25], index=["apple", "banana", "cherry"])
Task:
● Add both series
● Find the total sales of all fruits combined
'''

#importing modules
import pandas as pd

#shop tracks fruit sales
S1 = pd.Series([10,20,30], index = ["apple","banana","cherry"])
S2 = pd.Series([5, 15, 25], index=["apple", "banana", "cherry"])
print("Sales A")
print(S1)
print("--------------------------------------------")
print("Sales B")
print(S2)
print("--------------------------------------------")
#Add both series
S3 = S1 + S2
print("Cumulative Sales")
print(S3)
print("--------------------------------------------")
#Find the total sales of all fruits combined
total_sales = sum(S3)
print("Total Sales of given items are: ",total_sales)
print("--------------------------------------------")
