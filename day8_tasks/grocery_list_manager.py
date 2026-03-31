# Grocery List Manager
'''A user wants to save grocery items in a file grocery.txt.
Write a Python program that takes multiple items from the user and
writes them into the file, with each item on a new line.'''

import os

def grocery_list():
    try:
        if not os.path.exists("grocery.txt"):
            print("File not found!!")

            request = input("Do you want to create a file: [y/n] ")

            if request.lower() == 'n':
                print("Exiting...")
                return
            
            elif request.lower() == 'y':
                with open("grocery.txt", 'w') as grocery:
                    n = int(input("Enter number of items you want to add: "))
                    
                    for i in range(1, n + 1):
                        content = input("Enter list item: ")
                        grocery.write(f"{i}. {content}\n")
                
                print("Items added successfully")
                print("----------------------------------------------------\n")

        # Read file (common for both cases)
        with open("grocery.txt", 'r') as file:
            items = file.read()

        print("Successfully read the content!!")
        print(items)

    except FileNotFoundError:
        print("File not found!! Please check the file name or path")

grocery_list()

            

        
        
        
