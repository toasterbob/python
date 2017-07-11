# Looking for a benefactor
import math

def new_avg(arr, newavg):
    if len(arr) == 0 or arr[-1] <= 0:
        raise ValueError('Last value is not positive')
    target = (len(arr) + 1) * newavg
    donation = target - sum(arr)
    if donation <= 0:
        raise ValueError('Donation is not positive')
    return math.ceil(donation)


# ruby
def new_avg(arr, newavg)
  raise "ERROR" if arr[-1] <= 0 || arr.empty?
  target = (arr.length + 1) * newavg
  donation = target - arr.reduce(:+)
  raise "ERROR" if donation <= 0
  donation.ceil
end

p new_avg([14, 30, 5, 7, 9, 11, 15], 30)
