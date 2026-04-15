'''
3. Shopping Cart System
Scenario: A user adds items to a shopping cart.
Task:
● Store items in a list
● Convert to set to remove duplicates
● Use loop + condition to calculate total cost
● Handle invalid input using try-except
'''

#defining a function
def shopping_cart_system():
    try:
        #creation of shopping products list
        n = int(input("enter number of items to be stored: "))
        products = []
        item_prices = {}
        for i in range(n):
            product = input("enter product name: ")
            products.append(product)
            price = int(input("enter product price: "))
            item_prices[product] = price
        print(products)
        print(item_prices)
        print("---------------------------------------------------")

        #converting items into a set to remove duplicates
        unique_items = set(products)
        print("The unique products existing in the list are: ")
        print(unique_items)
        print("---------------------------------------------------")

        #Use Loop + Condition to calculate total cost
        total = 0
        for item in unique_items:
            try:
                if item in item_prices:
                    total += item_prices[item]
                else:
                    raise ValueError("Item not found")
            except ValueError:
                print(f"{item} is not available in cart")
        print("Total Cost: ",total)

    except ValueError:
        print("Please enter required input only integers allowed!!")
    
shopping_cart_system()
