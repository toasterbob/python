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



# range

# In Python we can also create ranges, which represent a range of numbers,
# with the following syntax: range(start,stop,step). Note that the range
# is not inclusive. In other words, range(1,4) will include 1, 2, and 3,
# but not 4!

# We can do some pretty cool things with range

(a,b,c,d) = range(4)
a # 0
b # 1
c # 2
d # 3

(a,b,c,d) = range(0, 8, 2)
a # 0
b # 2
c # 4
d # 6

for num in range(4,10):
    print(num)

# 4
# 5
# 6
# 7
# 8
# 9

# Note that the chr functions takes in a number
# and returns the ascii character for the number
capital_letters = []
for num in range(65, 91):
    capital_letters.append(chr(num))

capital_letters
# Output:['A','B','C','D','E','F','G','H','I','J',
#   'K','L','M','N','O','P','Q','R',
#   'S','T','U','V','W','X','Y','Z']



# Ranges take up less memory than lists, so if you find yourself needing a
# bunch of numbers that increment by the same amount each time, try to use
# a range instead of a list.

# List Comprehension

# List comprehensions are one of the most powerful tools in Python. They
# allow you to build lists in a more concise way, often in a single line.
# List comprehensions are a wonderful alternative to loops!

# One way to use a list comprehension is to transform a set of values from
# a range or another list into some new set of values. This is sometimes
# referred to as a mapping opration.

# return a list of squares
[num**2 for num in range(10)] # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

[chr(num) for num in range(65, 91)]
# Output:['A','B','C','D','E','F','G','H','I','J',
#   'K','L','M','N','O','P','Q','R',
#   'S','T','U','V','W','X','Y', 'Z']


# We can also put if statements inside of our list comprehensions to
# filter out certain transformed values!
# option 1 without list comprehension
vowels = []
for letter in 'awesome':
    if letter in ['a','e','i','o','u']:
        vowels.append(letter)

print(vowels) # ['a', 'e', 'o', 'e']

# option 2 with list comprehension
# In this example, the first letter is the value that we want in the new list
# and the if portion is the filter step
vowels = [letter for letter in "awesome" if letter in ["a", "e", "i", "o", "u"]]
print(vowels) # ['a', 'e', 'o', 'e']


# Count of 3 letter words in a string
len([word for word in "the quick brown fox jumps over the lazy dog".split(" ") if len(word) == 3 #4
# figure out the length
    # for each word in the string "the quick brown fox jumps over the lazy dog" split(" ") into an array
        # if the length of each word is 3
#
