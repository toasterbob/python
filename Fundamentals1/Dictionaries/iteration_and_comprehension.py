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
