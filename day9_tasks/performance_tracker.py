#Performance Tracker
'''
A software team wants to track how long functions take to execute.
Create a decorator that measures and prints the execution time of a
function.

'''
import time
def performance_tracker(func):

    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("Execution time of the function is: ",end_time - start_time)
    return wrapper

@performance_tracker
def track():
    for i in range(1000):
        pass
track()
    
