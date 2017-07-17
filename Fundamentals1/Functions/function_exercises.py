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









#
