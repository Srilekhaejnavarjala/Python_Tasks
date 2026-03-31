#Word counter program
'''
A writer saves an article in a file called article.txt. Write a Python program that:
● Opens and reads the file
● Counts the number of words, lines, and characters in the file
● Displays the results.
'''

import os
def word_count_program():
    try:
        if not os.path.exists("article.txt"):
            print("File not found.. Lets create...")
            
        with open("article.txt",'w') as file:
            text = input("enter article content: \n")
            file.write(text)
        print("File created successfully!\n")

        #reading file
        with open("article.txt",'r') as file:
            content = file.read()

        #count characters
        char_count = len(content)

        #count words
        words = content.split()
        word_count = len(words)

        #count lines
        lines = content.split("\n")
        line_count = len(lines)

        #displaying results
        print("Number of characters: ",char_count)
        print("Number of words: ",word_count)
        print("Number of lines: ",line_count)

    except FileNotFoundError:
        print("File not found. Pleace check file name.")

word_count_program()
