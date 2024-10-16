import sys

f = sys.stdin.read().splitlines()

# option 1
f = [list(map(int, item.split())) for item in f]

gears = [364, 66, 242, 675]
gears.sort()

# could only save the min max values
print(1.0 * gears[-1] / gears[0])

total = 1.0
for i in range(1, len(gears)):
    total *= gears[i] / gears[i - 1]
print(total)

# can optimize the list with a deque later.