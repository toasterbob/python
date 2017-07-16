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






#
