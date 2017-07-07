# Dictionary iteration

d = dict(name = 'Elie', job = 'Instructor')

for k in d:
    print(k)

# name
# job


# If you want access to both the keys and the values, call items on the
# dictionary and iterate through the result
d = dict(name = 'Elie', job = 'Instructor')

for key, value in d.items():
    print("{}: {}".format(key,value))

# name:Elie
# job:Instructor



# Dictionary comprehension

# - We can convert dictionaries into lists using list comprehension
d = {'a': 1, 'c': 3, 'e': 5}
[v for k,v in d.items()] # [1, 5, 3]
[k for k,v in d.items()] # ['a', 'e', 'c']

[[k,v] for k,v in d.items()] # [['a', 1], ['c', 3], ['e', 5]]


# But we can also convert other data types into dictionaries using dictionary comprehension!
str1 = "ABC"
str2 = "123"
{str1[i]: str2[i] for i in range(0,len(str1))} # {'A': '1', 'B': '2', 'C': '3'}


{ num:("even" if num % 2 == 0 else "odd") for num in range(1,5)
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}

# theirs
num_list = [1,2,3,4]
{ num:("even" if num % 2 == 0 else "odd") for num in num_list }



# Tuples

# Tuples are another collection in Python, but they are immutable.
# This means that you can't reassign values in tuples like you can with lists.
# Because of this immutability, however, operations on tuples are faster than lists.
# If you're defining a collection of values that won't change, use a tuple instead of a list.

x = (1,2,3)
3 in x # True
x[0] = "change me!" # TypeError: 'tuple' object does not support item assignment

#Tuple methods

# count - Returns the number of times a value appears in a tuple
x = (1,2,3,3,3)
x.count(1) # 1
x.count(3) # 3

# index - Returns the index at which a value is found in a tuple.
t = (1,2,3,3,3)
t.index(1) # 0
t.index(5) # ValueError: tuple.index(x): x not in tuple
t.index(3) # 2 - only the first matching index is returned




# Sets
# Sets do not have duplicate values, and elements in sets aren't ordered.
# You cannot access items in a set by index. Sets can be useful if you need
# to keep track of a collection of elements, but don't care about ordering.

# To test whether a value is a member of a set, use the in operator

# Sets cannot have duplictes
s = set({1,2,3,4,5,5,5}) # {1, 2, 3, 4, 5}# Creating a new set
s = set({1,4,5})

# Creating a new set
s = set({1,4,5})

# Creates a set with the same values as above
s = {4,1,5}


4 in s # True

8 in s # False


# Set methods

# add - Adds an element to a set. If the element is already in the set, the set doesn't change
s = set([1,2,3])
s.add(4)
s # {1, 2, 3, 4}
s.add(4)
s # {1, 2, 3, 4}

# clear - Removes all the contents of the set
s = set([1,2,3])
s.clear()
s # set()

# copy - Creates a copy of the set
s = set([1,2,3])
another_s = s.copy()
another_s # {1, 2, 3}
another_s is s # False
another_s.add(4)
another_s # {1, 2, 3, 4}
s # {1, 2, 3}

# difference - Returns a new set containing all the elements that are in
# the first set but not in the set passed to difference
set1 = {1,2,3}
set2 = {2,3,4}
set1.difference(set2) # {1}
set2.difference(set1) # {4}

# intersection - Returns a new set containing all the elements that are in both sets

set1 = {1,2,3}
set2 = {2,3,4}
set1.intersection(set2) # {2,3}

# symmetric_difference - Returns a new set containing all the elements
# that are in exactly one of the sets

set1 = {1,2,3}
set2 = {2,3,4}
set1.symmetric_difference(set2) # {1,4}

# union - Returns a new set containing all the elements that are in either set

set1 = {1,2,3}
set2 = {2,3,4}
set1.union(set2) # {1,2,3,4}
#
