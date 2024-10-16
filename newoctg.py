import sys
import math
from collections import defaultdict

f = sys.stdin.read().splitlines()

# option 1
f = [list(map(int, item.split())) for item in f]

mydict = defaultdict(list)

for size, ratio in f[1:]:
    mydict[size].append(ratio)

total = 1.0

maxremaining = float("-inf")

for gears in mydict.values():
    gears.sort()

    # can optimize the list with a deque later.
    # when sublist is length 1, cannot do more stuff. - stop

    left, right = 0, len(gears) - 1
    #TODO : check if length is 2 or larger
    # could only save the min max values
    while right - left >= 1:
        total *= gears[right] / gears[left]

        right -= 1
        left += 1
    if left == right:
        maxremaining = max(gears[left], maxremaining)

if maxremaining != float("-inf"):
    total *= maxremaining

print(math.log(total))