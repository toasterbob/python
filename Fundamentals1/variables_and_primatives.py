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

# Unicode represents each letter, character, or ideograph as a 4-byte
# number. Each number represents a unique character used in at least one
# of the world’s languages. (Not all the numbers are used, but more than
# 65535 of them are, so 2 bytes wouldn’t be sufficient.)

# 4 bytes is  2 ** 32 = 4294967296

# Characters that are used in multiple languages generally have the same
# number, unless there is a good etymological reason not to. Regardless,
# there is exactly 1 number per character, and exactly 1 character per
# number. Every number always means just one thing; there are no “modes”
# to keep track of. U+0041 is always 'A', even if your language doesn’t
# have an 'A' in it.

# Four bytes? For every single character‽ That seems awfully wasteful,
# especially for languages like English and Spanish, which need less than
# one byte (256 numbers) to express every possible character.

# There is a Unicode encoding that uses four bytes per character. It’s
# called UTF-32, because 32 bits = 4 bytes. UTF-32
# This has some advantages, the most important being that you can find
# the Nth character of a string in constant time, because the Nth
# character starts at the 4×Nth byte
# DISADVANTAGE - 4 bytes per character file size

#Even though there are a lot of Unicode characters, it turns out that
# most people will never use anything beyond the first 65535.

# UTF-16 (because 16 bits = 2 bytes). UTF-16 encodes every character
# from 0–65535 as two bytes
# twice as space-efficient as UTF-32
#you can still easily find the Nth character of a string in constant time
# if you assume that the string doesn’t include any astral plane characters,
# which is a good assumption right up until the moment that it’s not.

# But there are also non-obvious disadvantages to both UTF-32 and UTF-16.
# Different computer systems store individual bytes in different ways.
# To solve this problem, the multi-byte Unicode encodings define a “Byte
# Order Mark,” which is a special non-printable character that you can
# include at the beginning of your document to indicate what order your bytes are in.

#UTF-8
# UTF-8 is a variable-length encoding system for Unicode. That is,
# different characters take up a different number of bytes. For ascii
# characters (A-Z, &c.) utf-8 uses just one byte per character. In fact,
# it uses the exact same bytes; the first 128 characters (0–127) in
# utf-8 are indistinguishable from ascii.
# “Extended Latin” characters like ñ and ö end up taking two bytes.
# Chinese characters like 中 end up taking three bytes.
# The rarely-used “astral plane” characters take four bytes.

# Disadvantages: because each character can take a different number of
# bytes, finding the Nth character is an O(N) operation — that is, the
# longer the string, the longer it takes to find a specific character.
# Also, there is bit-twiddling involved to encode characters into bytes
# and decode bytes into characters.

# Advantages: super-efficient encoding of common ascii characters. No
# worse than UTF-16 for extended Latin characters. Better than UTF-32 for Chinese characters.
# due to the exact nature of the bit twiddling, there are no byte-ordering issues
# A document encoded in utf-8 uses the exact same stream of bytes on any computer.

a = "hello"
len(a) # 5
# A string is like a tuple of characters.

string = "this Is nIce"
string.upper() # 'THIS IS NICE'
string.lower() # 'this is nice'
string.title() # 'This Is Nice'

# Find
# To find a subset of characters in a string we can use the find method.
# This will return the index at which the first match occurs. If the
# character/characters is/are not found, find will return -1

instructor = 'elie'
instructor.find('e') # 0
instructor.find('E') # -1 it IS case sensitive!
string.find("i") # 2, since the character "i" is at index 2
string.find('Tim') # -1
