# Looking for a benefactor
def new_avg(arr, newavg):
    if arr[-1] <= 0:
        raise ValueError('Last value is not positive')
    target = (len(arr) + 1) * newavg
    donation = target - sum(arr)
    if donation <= 0:
        raise ValueError('Donation is not positive')
    return donation
