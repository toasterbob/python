# Reversed strings
def solution(str):
    return str[::-1]


# Looking for a benefactor
import math

def new_avg(arr, newavg):
    target = (len(arr) + 1) * newavg
    donation = target - sum(arr)
    if donation <= 0:
        raise ValueError('Donation is not positive')
    return math.ceil(donation)


# ruby
def new_avg(arr, newavg)
  raise "ERROR" if arr[-1] <= 0 || arr.empty?
  target = (arr.length + 1) * newavg
  donation = target - arr.reduce(0,:+)
  raise "ERROR" if donation <= 0
  donation.ceil
end

p new_avg([14, 30, 5, 7, 9, 11, 15], 30)


# Sum of a sequence
def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number, end_number + 1, step))

# Ruby
def sequence_sum(begin_number, end_number, step)
  sum = 0
  while begin_number <= end_number
    sum += begin_number
    begin_number += step
  end
  sum
end
# Ruby 2
def sequence_sum(begin_number, end_number, step)
  arr = (begin_number..end_number).step(step).to_a
  arr.reduce(0, :+)
end


# max diff
def max_diff(arr):
    if len(arr) <= 1:
        return 0
    arr.sort()
    return arr[-1] - arr[0]

def max_diff(arr):
    return max(arr) - min(arr) if arr else 0
# for 1 value array it would equal zero

# Ruby
def max_diff(arr)
    if arr.empty?
        0
    else
        arr[-1] - arr[0]
    end
end

# count smiley faces
def count_smileys(arr):
    count = 0
    for el in arr:
        if el[0] == ":" or el[0] == ";":
            if el[1] == ")" or el[1] == "D":
                count += 1
            elif el[1] == "-" or el[1] == "~":
                if el[2] == ")" or el[2] == "D":
                    count += 1
    return count

import re
def count_smileys(arr):
    return sum(1 for _ in re.finditer(r"[:;][-~]?[)D]", " ".join(arr)))

from re import findall
def count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))
