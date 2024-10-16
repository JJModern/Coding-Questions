import sys
import math
from collections import deque
from collections import defaultdict

f = sys.stdin.read().splitlines()

# option 1
f = [list(map(int, item.split())) for item in f]

mydict = defaultdict(list)

for size, ratio in f[1:]:
    mydict[size].append(ratio)

for key in mydict:
    mydict[key] = deque(sorted(mydict[key]))

total = 1.0

# can optimize the list with a deque later.
# when sublist is length 1, cannot do more stuff. - stop
biglist = deque(mydict.values())
while biglist:
    gears = biglist.popleft()
    #TODO : check if length is 2 or larger
    # could only save the min max values
    if len(gears) >= 2:
        total *= gears.pop() / gears.popleft()

        if len(biglist) <= 0:
            break
        else:
            biglist.append(gears)

print(math.log(total))