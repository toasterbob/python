# Scope
# In Python we have function scope, which prohibits us from accessing
# variables created inside of a function from outside of that function
def func():
    x = 5
    return x

func() # 5
x # NameError


# The global keyword
# The global scope includes all variables defined outside of functions.

# But if we try to use a global variable in a method, we will see
# UnboundLocalError: local variable VARIABLE_NAME referenced before assignment

# This happens because a method in Python either has local variables or
# global variables. If variable is defined anywhere in a method and that
# variable has the same name as a global variable, then the new local
# variable will be used in the function instead of the global. But if you
# actually want to assign a global variable from within a function, you
# need to use the global keyword. Using global variables in general
# is not best practice

id = 0
def increment_id():
    id += 1

increment_id() # UnboundLocalError: local variable 'id' referenced before assignment

# In Python you need to explicitly state that a variable should be global, using the global keyword.
id = 0
def increment_id():
    global id
    id += 1

increment_id() # The global id is now 1


# Listing locals and globals
# In Python we can display all of the local variables and global variables
# using the locals and globals functions

def print_locals():
    x = 2
    name = "Elie"
    print(locals())

print_locals() #{'name': 'Elie', 'x': 2}

print(globals())
print(locals())


# Python Nested Functions (sort of like closures)

# In Python we do have support for closures, a feature where an inner
# function has access to variables in an outer function's scope, even
# after the outer function has finished executing.

def outer(a):
    def inner(b):
        return a + b
    return inner

outer(3)(4) #7
x = outer(2)
x(10) #12


# However, closures in Python are "weak" and have some limitations. For example,
# if you want to change the value of a variable from an outer scope,
# you'll run in to problems:

def counter():
    x = 0;
    def increment():
        x += 1
        print(x)
    return increment

counter()() # UnboundLocalError: local variable 'x' referenced before assignment


def outerCount():
    def innerCount():
        innerCount.x += 1
        print(innerCount.x)
    innerCount.x = 0
    return innerCount

x = outerCount()
x() # 1

y = outerCount()
y() # 1

x() # 2



# Documenting our functions

# Something that Python offers us is the ability to add what is called a docstring

def say_hello():
    # we are using three quotes so that this can be a multi-line string if necessary
    """This function returns the string hello when called"""
    return "hello"

say_hello() # "hello"

say_hello.__doc__ # "This function returns the string hello when called"

help(say_hello) # gives us even more detail with the docstring!

# Docstrings are essential when writing methods and can be thought of like
# an enhanced comment. Docstrings are also very useful when writing tests,
# as you can see what the docstring is when running the test.


#
