a = 1
b = "YOLO"
nothing = None

# multiple assignment
a, b = 1, 2
a # 1
b # 2

# variables in snake case
my_variable = 3
my_variable2 = 4

#types
type(False) # bool
type("nice") # string
type({}) # dict
type([]) # class list
type(()) # class tuple - Tuples are lists with immutable values - uses parentheses (4, 2, 1)
type(None) # class NoneType

# Strings - in Python 3, all strings are represented in Unicode.
# The most popular character encoding that is dominant on the web now is
# UTF-8, which uses 8-bit code units, but with a variable length to ensure
# that all sorts of characters can be encoded.

# Then there are languages like Chinese, Japanese, and Korean, which
# have so many characters that they require multiple-byte character sets.
# That is, each “character” is represented by a two-byte number from 0–65535
# Two bytes is 2 ** 16 = 65536

# Well, systems had to be designed to carry encoding information along
# with every piece of “plain text.” Remember, it’s the decryption key
# that maps computer-readable numbers to human-readable characters. A
# missing decryption key means garbled text, gibberish, or worse.

# UNICODE 
# Unicode is a system designed to represent every character from every language.
