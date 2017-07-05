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
