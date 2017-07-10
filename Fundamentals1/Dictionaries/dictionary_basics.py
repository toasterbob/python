# Dictionaries

# Dictionaries in Python are key-value pairs.
# To access a value in a dictionary, you pass the key in using square brackets.

# There are a few different ways to create a dictionary. One is to use curly
# braces, separating key-value pairs by a comma, and placing a colon
# between the key and the value

authors = {
    'Great Gatsby': 'F Scott Fitzgerald',
    'Slaughterhouse Five': 'Kurt Vonnegut',
    'Of Mice and Men': 'John Steinbeck'
}

authors['Great Gatsby'] == 'F Scott Fitzgerald' # True


# Another approach is to use the dict function. In this case, you can assign
# values to keys directly using =
another_dictionary = dict(key = 'value')
another_dictionary # {'key': 'value'}
another_dictionary['key'] == 'value' # True
another_dictionary['another_key'] # KeyError

another_dictionary['another_key'] = 3
another_dictionary['another_key'] # 3

# Note that if you try to access a value with a key that doesn't exist in
# the dictionary, Python will throw an error.

another_dictionary = dict(key = 'value')
another_dictionary['key'] = 'new value'
another_dictionary['another_key'] = 'another value'
another_dictionary # {'another_key': 'another value', 'key': 'new value'}











#
