def first_function():
    print("Hello World!")

first_function() #"Hello World!"

def add_five_plus_five():
    return 5 + 5

print(add_five_plus_five())

ten = add_five_plus_five()
print(ten + 10) #20

def return_none():
    "hi" #no return

var = return_none();
print(var) # None
print(var == None) # true
