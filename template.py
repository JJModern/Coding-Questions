import sys

f = sys.stdin.read().splitlines()

# option 1
f = [list(map(int, item.split())) for item in f]

#############

# option 2
num = int(f[0])

for i in range(1, num + 1):
    f[i * 2]



num = f[0][0]
