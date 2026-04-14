'''
5. Adding and Updating Columns
A DataFrame:
df = pd.DataFrame({
"Price": [100, 200, 300]
})
Scenario:
● Add a column Discount = 10% of Price
● Add another column Final Price = Price - Discount
'''

#importing pandas
import pandas as pd

#dataframe
df = pd.DataFrame({
"Price": [100, 200, 300]
})
print("Original Data Frame")
print(df)
print("----------------------------------------------------")

#Adding a column discount of 10% of price
df['Discount'] = df['Price']*0.1
print("Data Frame after adding Discount column")
print(df)
print("----------------------------------------------------")

#Adding another column Final Price
df['Final_Price'] = df['Price']-df['Discount']
print("Data Frame after adding Final Price Column")
print(df)
print("----------------------------------------------------")
