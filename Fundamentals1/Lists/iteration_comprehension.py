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

# If you ever want to move to the next step of the iteration, you can
# prematurely break out of the current iteration with the the continue
# keyword. Similarly, you can exit from a loop entirely using the break keyword.

for num in [1, 2, 3, 4, 5, 6, 7]:
    if num % 2 == 0:
        continue
    elif num > 5:
        break
    print(num)

# 1
# 3
# 5
# the loop continues before the print statement if num is even,
# and it ends entirely when num is 6, so the last odd number doesn't get printed.   













#
