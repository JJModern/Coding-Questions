import sys

f = sys.stdin.read().splitlines()
f = [list(map(int, item.split())) for item in f]

r = f[0][0]
c = f[0][1]

res = r
for _ in range(c - 1):
    res *= (r - 1)

print(res % 998244353)