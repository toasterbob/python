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




#
