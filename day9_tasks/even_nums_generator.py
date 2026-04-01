#Infinite even number generator (Generator)
'''
Create a generator function that continuously generates even numbers
starting from 2. The program should print the first N even numbers
using this generator.

'''
def even_numbers():
    num = 2
    while True:
        yield num
        num += 2
n = int(input("enter how many even numbers: "))
count = 0
for i in even_numbers():
    print(i)
    count += 1
    if count == n:
        break
    
    

