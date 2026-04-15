'''
9. Smart Data Processing Pipeline
Scenario:
A system processes numeric data from file.
Task:
● Read numbers from a file
● Use NumPy for calculations (mean, std)
● Convert results to Pandas DataFrame
● Use exception handling for bad data
● Use a generator to stream data
● Apply decorator to measure execution time
'''

#importing modules
import numpy as np
import pandas as pd
import time

# decorator for execution time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution Time:", end - start)
        return result
    return wrapper


# generator to read file
def stream_file():
    try:
        with open("numbers.txt", 'r') as f:
            for line in f:
                try:
                    yield int(line.strip())
                except ValueError:
                    print("Invalid data skipped:", line)
    except FileNotFoundError:
        print("File not found!")


nums = []  

while True:
    print("\n1. Read Numbers from a file")
    print("2. Calculate mean and Std Deviation")
    print("3. Results to Pandas DF")
    print("4. Generator to stream data")
    print("5. Calculate execution time")
    print("6. Exit")

    option = int(input("enter option to continue: "))

    if option == 1:
        choice = input("do you want to create a file? (Y/N) ")
        if choice.lower() == 'y':
            nums = np.random.randint(100, 500, 10)

            try:
                # FIXED: write instead of append
                with open("numbers.txt", 'w') as f:
                    for num in nums:
                        f.write(str(num) + "\n")

                print("Numbers written successfully:", nums)

                # reading file properly
                with open("numbers.txt", 'r') as t:
                    data = t.read()
                    print("File content:\n", data)

            except Exception:
                print("Error while handling file")

    elif option == 2:
        if len(nums) == 0:
            print("No data available! First create/read file.")
        else:
            average_nums = np.mean(nums)
            print("Average:", average_nums)

            std_nums = np.std(nums)
            print("Standard Deviation:", std_nums)

    elif option == 3:
        if len(nums) == 0:
            print("No data available!")
        else:
            results = pd.DataFrame(nums, columns=["Numbers"])
            print("Pandas DataFrame:")
            print(results)

    elif option == 4:
        print("Streaming data using generator:")
        for val in stream_file():
            print(val)

    elif option == 5:
        @timer
        def execution_time():
            for i in range(1000000):
                pass

        execution_time()

    elif option == 6:
        print("Exiting...")
        break
                
                

            
                
    
