import sys

f = sys.stdin.read().splitlines()
f = [list(map(int, item.split())) for item in f]

for a, b in f[1:]:
    print((b - a % b) % b)