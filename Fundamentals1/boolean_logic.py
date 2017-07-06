# Conditionals
# with if/else statements. One difference with Python, however, is that
# it does not use the else if construct for chaining multiple conditions
# together
# Python uses the keyword elif (short for else if).

#elif
# Note also that Python does not require parenthesis around conditions,
# but each condition must end with a :
 # If you forget the colon (a very common mistake when you're first learning
 # Python!), you'll get a SyntaxError

user = 'Tom'
if user == 'Elie':
    print('Awesome!')
elif user == 'Tom':
    print('Cool!')
else:
    print('Nope!')

user = 'Mark'
if user == "Mark":
    print("Awesome Sauce")


# Python also allows you to use words like or, and, and not for comparison
if 1 > 2 or 2 > 1:
    print("cool")

if 1 == 1 and 2 == 2:
    print("nice!")

if not False: #not false == true
    print("it is true!")

# One nice thing about comparing numbers is that you can string inequalities
# together without using the and keyword:
if 1 < 2 and 2 < 3:
    print("this is ok")

if 1 < 2 < 3:
    print("this is better!")

# Also, it's important to understand that the indentation in all of
# these examples matters tremendously. Indentation is how Python keeps
# track of what code should be executed conditionally, and which code
# should always be executed:


name = "Mark"
if name == "Mark":
    print("Your name is Mark")
print("Bye!")
# In the example above, both messages will be printed. But if you change
# the name variable to something besides "Mark", the second print
# statement will still execute.

# name = "Matt"
# if name == "Matt":
# print("Your name is Matt") # IndentationError!


# Falsey Values in Python
# Python has quite a few falsey values (values that evaluate to False
# when converted to a boolean). We can check whether a value is falsey
# by passing it into the bool function! All of the following examples
# evaluate to false when converted to a boolean.

# False
bool(False)

# 0
bool(0)

# None
bool(None)

# Empty string
bool("")

# Empty list
bool([])

# Empty tuple
bool(())

# Empty dictionary
bool({})

# Empty set
bool(set())













#
