
def pet_names(cat_name, dog_name):
    return "I have a cat named {} and a dog named {}".format(cat_name, dog_name)

print(pet_names("bob", "cat"))

#keyword arguments
def pet_names(cat_name, dog_name):
    return "I have a cat named {} and a dog named {}.".format(cat_name, dog_name)

# no keyword arguments - order matters!
pet_names("Mittens", "Fido") # "I have a cat named Mittens and a dog named Fido."

pet_names("Fido", "Mittens") # "I have a cat named Fido and a dog named Mittens." -- uh oh, the names are the opposite of what we want, because we passed them to the function in the wrong order.

# keyword arguments
pet_names(cat_name="Mittens", dog_name="Fido")
# "I have a cat named Mittens and a dog named Fido."

# keyword arguments - order doesn't matter!
pet_names(dog_name="Fido", cat_name="Mittens")
# "I have a cat named Mittens and a dog named Fido."

# When you call a function by passing in a keyword=value pair, you're said to be using keyword arguments.
# This can be especially useful if you have a function that accepts many parameters.


# Default argument values
def add(a=5,b=15):
    return a + b

add(15,1) # 16
add(4) # 19 - a is set to 4, b is set to 15
add() # 20
add(b=30) # 35 - a is set to 5 by default and b is 30 using keyword arguments



# Variable number of function arguments
# There are two ways we can do this. The first is by using *

def foo(*args):
    print(args)

foo(1,2,3)
foo(1,2)
foo([1, 2, 3])
# Inside of the function, the named parameter after the * corresponds to
# a tuple of the arguments passed in.
