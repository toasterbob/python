
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




# Returning Functions
# Python also allows you to return functions from other functions.

def parent(num):
    def first_child():
        return "Printing from the first_child() function."
    def second_child():
        return "Printing from the second_child() function."

    try:
        assert num == 10
        return first_child
    except AssertionError:
        return second_child

foo = parent(10)
bar = parent(11)

print(foo) # <function parent.<locals>.first_child at 0x101d0c840>
print(bar) # <function parent.<locals>.second_child at 0x101d0c8c8>

print(foo()) # Printing from the first_child() function.
print(bar()) # Printing from the second_child() function.




# Decorators
# example 1
def my_decorator(some_function):
    def wrapper():
        print("Something is happening before some_function() is called.")
        some_function()
        print("Something is happening after some_function() is called.")
    return wrapper


def just_some_function():
    print("Wheee!")


just_some_function = my_decorator(just_some_function)

just_some_function()
# Something is happening before some_function() is called.
# Wheee!
# Something is happening after some_function() is called.


# example 2
def my_decorator(some_function):
    def wrapper():
        num = 10
        if num == 10:
            print("Yes!")
        else:
            print("No!")
        some_function()
        print("Something is happening after some_function() is called.")
    return wrapper


def just_some_function():
    print("Wheee!")

just_some_function = my_decorator(just_some_function)

just_some_function()
# Yes!
# Wheee!
# Something is happening after some_function() is called.


# Syntactic sugar!
# Python allows you to simplify the calling of decorators using the @ symbol (this is called “pie” syntax).


#
