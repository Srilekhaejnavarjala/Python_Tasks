'''
7. Generator-based Log Reader
Scenario:
A large log file needs to be processed.
Task:
● Create a generator to read file line by line
● Use loop to process logs
● Use condition to filter errors
● Count occurrences using a dictionary
'''

# Generator function to read file line by line
def read_logs(file_name):
    with open(file_name, "r") as f:
        for line in f:
            yield line.strip()


def process_logs():
    error_count = {}   

    try:
        for log in read_logs("log.txt"):   
            
            # filter only ERROR logs
            if "ERROR" in log:
                print("Error log found:", log)

                # count occurrences
                if log in error_count:
                    error_count[log] += 1
                else:
                    error_count[log] = 1

        print("\nError Count:")
        print(error_count)

    except FileNotFoundError:
        print("Log file not found!")

        choice = input("Do you want to create the file? (Y/N): ")

        if choice.lower() == 'y':
            with open("log.txt", "w") as f:
                print("File created successfully (empty file).")

            print("Run the program again after adding logs.")
        else:
            print("File not created. Exiting program.")


process_logs()
