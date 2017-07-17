def difference(a: int, b: int) -> int:
    return a - b

difference(2,2) # 0
difference(0,2) # -2


def product(a, b):
    return a * b

product(2,2) # 4
product(0,2) # 0


def print_day(a: int):
    if a < 1 or a > 7:
        return None
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return days[a - 1]

print_day(4) # "Wednesday"
print_day(41) # None


#theirs
def print_day(n):
    try:
        return ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][n - 1]
    except IndexError as e:
        return None

print_day(4) # "Wednesday"
print_day(41) # None


def last_element(arr):
    try:
        return arr[-1]
    except IndexError as e:
        return None

last_element([1,2,3,4]) # 4
last_element([]) # None


def number_compare(a, b):
    if a > b:
        return "First is greater"
    elif a < b:
        return "Second is greater"
    else:
        return "Numbers are equal"

number_compare(1,1) # "Numbers are equal"
number_compare(1,2) # "Second is greater"
number_compare(2,1) # "First is greater"

# theirs has no else
def number_compare(a,b):
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    return "Numbers are equal"

def single_letter_count(word, letter):
    return word.lower().count(letter.lower())

single_letter_count('amazing','A') # 2


def multiple_letter_count(word):
    return { char: word.count(char) for char in word }

multiple_letter_count("hello") # {h:1, e: 1, l: 2, o:1}
multiple_letter_count("person") # {p:1, e: 1, r: 1, s:1, o:1, n:1}


def list_manipulation(list, command, location, value = None):
    if command == "remove":
        if location == "end":
            return list.pop()
        elif location == "beginning":
            return list.pop(0)
    elif command == "add":
        print('hi')
        if location == "end":
            list.append(value)
            return list
        elif location == "beginning":
            list.insert(0, value)
            return list

list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") # 1
list_manipulation([1,2,3], "add", "beginning", 20) # [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) # [1,2,3,30]


# theirs
def list_manipulation(collection, command, location, value=None):
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0,value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection

def is_palindrome(word):
    word = word.replace(" ", "") # remove whitespace
    return word.lower() == word.lower()[::-1]

is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('a man a plan a canal Panama') # True


def frequency(list, item):
    return list.count(item)

frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1


def flip_case(string, case):
    result = [letter.swapcase() if letter.lower() == case.lower() else letter for letter in string]
    return "".join(result)

flip_case("Hardy har har", "h") # "hardy Har Har"

#theirs
def flip_case(string, letter):
    return "".join([char.swapcase() if char.lower() == letter.lower() else char for char in string])



def multiply_even_numbers(list):
    result = 1
    for num in list:
        if num % 2 == 0:
            result *= num
    return result

multiply_even_numbers([2,3,4,5,6]) # 48

#theirs
def multiply_even_numbers(list):
    # you can import reduce from the functools module if you would like
    total = 1
    for val in list:
        if val % 2 == 0:
            total = total * val
    return total


def mode(list):
    high = 0
    val = None
    dictionary = {num: list.count(num) for num in list}
    print(dictionary)
    for k,v in dictionary.items():
        if v > high:
            high = v
            val = k
    return val

mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4

def mode(nums):
    dictionary = {num: nums.count(num) for num in nums}
    max_value = max(dictionary.values())
    idx = list(dictionary.values()).index(max_value)
    return list(dictionary.keys())[idx]

mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4



#theirs

def mode(collection):
    # you can import mode from statistics to cheat
    # you can import Counter from collections to make this easier

    # or we can just solve it :)
    count = {val: collection.count(val) for val in collection}
    # find the highest value (the most frequent number)
    max_value = max(count.values())
    # now we need to see at which index the highest value is at
    correct_index = list(count.values()).index(max_value)
    # finally, return the correct key for the correct index (we have to convert cou)
    return list(count.keys())[correct_index]
#
