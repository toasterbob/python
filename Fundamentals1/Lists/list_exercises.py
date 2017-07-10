#List Comprehension
#1
list = [1, 2, 3, 4]
for num in list:
    print(num)

# theirs
[print(val) for val in [1,2,3,4]]

#mine
[print(num) for num in [1, 2, 3, 4]]

#2
list = [num * 20 for num in range(1,5)]
for num in list:
    print(num)

list = [1, 2, 3, 4]
for num in list:
    print(num * 20)

# theirs
[print(val*20) for val in [1,2,3,4]]

#mine
[print(num * 20) for num in [1, 2, 3, 4]]

#3
[name[0] for name in ["Elie", "Tim", "Matt"]]

#4
[num for num in [1,2,3,4,5,6] if num % 2 == 0]

#5
