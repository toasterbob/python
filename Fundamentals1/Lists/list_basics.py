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


# LIST METHODS

# append - Adds a value to the end of a list
my_list = [1,2,3]
my_list.append(10)
my_list # [1,2,3,10]

# clear - Removes all the values in a list:
l = [1,2,3]
l.clear()
l # []

# copy - Makes a copy of a list (like dup in Ruby)
l = []
l.append(2)
l.append(3)
l.append(4)
l # [2, 3, 4]
z = l.copy()
z # [2, 3, 4]
l # [2, 3, 4]
z.remove(3)
z # [2, 4]
l # [2, 3, 4]









#
