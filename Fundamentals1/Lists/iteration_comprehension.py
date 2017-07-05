# Iterating over lists and strings

# for in
#
# The most common way of iterating over a list is a for in loop.
# The syntax is for ELEMENT in LIST
# As with if statements, don't forget about the colon!

values = [1,2,3,4]
for val in values:
    print(val)

# 1
# 2
# 3
# 4

for char in "awesome":
    print(char)

# a
# w
# e
# s
# o
# m
# e

# Sometimes you may want to have access to the element's index in the list
# as well as the element itself. In this case, you can pass the list into
# the enumerate function.

# You'll need to name two variables in the for loop: the first will refer
# to the current index, the second will refer to the current element:

for idx, char in enumerate("awesome"):
    print(idx, char)

# 0 a
# 1 w
# 2 e
# 3 s
# 4 o
# 5 m
# 6 e


# while
#
# You can also do a while loop with Python, but this is a bit less common
# when iterating

i = 0
while i < 5:
    print(i)
    i +=1

# 0
# 1
# 2
# 3
# 4


#
