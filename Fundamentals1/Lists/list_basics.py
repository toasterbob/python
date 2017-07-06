# Lists

# Lists in Python are simply collections of elements.
number_list = [1, 2, 3, 4, 5]
string_list = ["a", "b", "c", "d"]
kitchen_sink_list = [4, "yo", None, False, True, ["another", "list"]]

# To access an element in a list, we use bracket notation and pass in
# the index we're interested in

my_list = ["a", 1, True]
my_list[0] # "a"
my_list[2] # True
my_list[3] # IndexError

# Note that if you try to access an element with an invalid index,
# Python will give you an error.
# UNLIKE RUBY

# We can also reassign values in lists using =

my_list = ["a", 1, True]
my_list[2] = False
my_list # ["a", 1, False]









#
