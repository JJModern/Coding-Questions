import sys
import math
import itertools

f = sys.stdin.read().splitlines()

return_set = set()
set_num_lst_low_high = []
# number of primes
for i in range(len(f) // 3):
    low, high = f[(i * 3) + 2].split()
    print(low, high)
    set_num_lst_low_high.append(
        [[int(x) for x in f[(i * 3) + 1].split()], int(low), int(high)]
    )

# 1 if included

# different combinations of the numbers


# squares of each number in range
def find_squares(num, low_bound, high_bound):
    min = math.ceil(math.log(low_bound, num))
    max = int(math.log(high_bound, num))
    if low_bound == 1 and low_bound <= high_bound:
        return_set.add(1)
    for i in range(min, max + 1):
        return_set.add(num**i)


find_squares(3, 1, 12)
print(return_set)

"""
def find_combos(set_num_lst_low_high):
    exponent_combos = []

    for item in set_num_lst_low_high:
        item, high_bound = item[0], item[2]
        max = int(math.log(high_bound, item))
        exponent_combos.append([i for i in range(max + 1)])
    exponent_combos = list(itertools.product(*exponent_combos))
    print(exponent_combos)
    for item in exponent_combos:
        total_multiply = 1
        for i, num in enumerate(item):
            total_multiply *= (set_num_lst_low_high[i][0] ** num)
        #can probably optimize here.
        #
        if low_bound <= total_multiply <= high_bound:
            return_set.add(total_multiply)
"""


# find_combos([[3, 20, 30]])
