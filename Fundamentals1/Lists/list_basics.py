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


# count - Counts how many times an item appears in a list
l = [1,2,3,4,5,5,5,5]
l.count(1) # 1
l.count(5) # 4

# extend - Appends another list and flattens the appended list
# (so there is not a list inside of a list):
l = [1,2,3]
l.append([4])
l # [1,2,3,[4]]

l.extend([5,6,7])
l # [1,2,3,[4],5,6,7]

l = [1,2,3]
l.extend([4])
l.extend([5,6,7])
l # [1,2,3,4,5,6,7]


# index - Returns the index at which a value is found. If the value is
# not found, index returns a ValueError:

l = [4, 8, 6, 4]
l.index(8) # 1
l.index(4) # 0 - it only finds the index of the first matching element
l.index(12) # ValueError

# insert - Takes in an index and a value, and inserts the value at the given index
l = [4,6,8]
l.insert(2, 'awesome')
l # [4,6,'awesome',8]

# pop - By default, pop removes the last element from a list. If pop is
# given an index as an argument, the element at that index is removed.
# This method returns the element removed
l = [3,4]
l.pop(0) # 3
l
l.pop() # 4
l.pop() # IndexError - Notice that pop throws an error if you call it on an empty list!

# In Ruby if you add a value to pop, it pops that many items, not the index

# remove - Removes the first occurrence of a value
l = [1,2,3,1]
l.remove(1)
l # [2,3,1]
l.remove(5) # ValueError - Notice that remove throws an error if you try
# to remove something not in the list.

# reverse - Reverses a list in place (i.e. it mutates the original list)
l = [1,2,3,4]
l.reverse()
l # [4,3,2,1]

# sort - Sorts the list in place (i.e. it mutates the original list)
l = [1,4,3,2]
l.sort()
l # [1,2,3,4]


# Slicing Lists
# Slices return portions of a list or string.

# Slices return portions of a list or string. While this seems like a
# pretty minor concept, there's actually quite a bit you can do with
# slices that you might not expect.

# The standard syntax for a slice is list[start:end], or list[start:end:step]
# We can also do list[:] to make a copy of a list,
# or even list[::-1] to make a copy of a reversed list.

first_list = [1,2,3,4,5,6]
first_list[0:1] # [1]

# if a value for end isn't provided, you'll slice to the end of the list
first_list[1:] # [2, 3, 4, 5, 6]

# if a value for start isn't provided, you'll slice from the start of the list
first_list[:3] # [1,2,3]

# get the last element in the list
first_list[-1] # 6

# start from the second to last element in the list
first_list[-2:] # [5, 6]

#
