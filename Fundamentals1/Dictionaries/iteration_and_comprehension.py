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










#
