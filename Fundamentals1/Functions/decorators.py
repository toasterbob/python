
# First Class Objects

# In Python, functions are first-class objects. This means that functions
# can be passed around, and used as arguments, just like any other value
def foo(bar):
    return bar + 1

print(foo)
print(foo(2))
print(type(foo))


def call_foo_with_arg(foo, arg):
    return foo(arg)

print(call_foo_with_arg(foo, 3))


# Nested Functions
# Because of the first-class nature of functions in Python, you can define
# functions inside other functions. Such functions are called nested functions.

def parent():
    print("Printing from the parent() function.")

    def first_child():
        return "Printing from the first_child() function."

    def second_child():
        return "Printing from the second_child() function."

    print(first_child())
    print(second_child())

parent()
# Printing from the parent() function.
# Printing from the first_child() function.
# Printing from the second_child() function

first_child() # Error

# Whenever you call parent(), the sibling functions, first_child() and
# second_child() are also called AND because of scope, both of the
# sibling functions are not available (e.g., cannot be called) outside of
# the parent function.



#
