'''
4. Conditional Discount System (List Comprehension)
A shop has prices:
prices = [100, 200, 300, 400]
Scenario:
● Apply a 10% discount only if price > 200.
Task:
● Use list comprehension with condition to create updated price list
'''


#defined list
prices = [100,200,300,400]
print("Original Prices: ",prices)

#condition
discounted_prices = [price * 0.9 if price > 200 else price for price in prices]
print("Updated Prices: ",discounted_prices)
