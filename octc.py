import sys

f = sys.stdin.read().splitlines()

# option 1
f = [list(map(int, item.split())) for item in f]

count = 0
for sublist in f[1:]:
    if sublist[0] % 2 != 0:
        count += 1
print(count)