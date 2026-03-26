"""7. Write a program to convert a tuple to a list and modify the element."""
tup = ("Hyderabad","Warangal","Secunderabad","Malakpet","Dilsukhnagar")
print("The tuple elements are: \n",tup)
print("-------------------------------------------------------------------\n")
#let us change secunderabad to LBNagar
li = list(tup)
li[2] = "LBNagar"
print("The elements in the tuple after modifying are: \n",tuple(li))
