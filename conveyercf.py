import sys

f = sys.stdin.read().splitlines()
f = [list(map(int, item.split())) for item in f]

def outer_level(x, y, n):
    return min(min(x - 1, n - x), min(y - 1, n - y))

for sub_lst in f[1:]:
    n = sub_lst[0]
    print(abs(outer_level(sub_lst[1], sub_lst[2], n) - outer_level(sub_lst[3], sub_lst[4], n)))
# 5
# 2 1 1 2 2
# 4 1 4 3 3
# 8 1 3 4 6
# 100 10 20 50 100
# 1000000000 123456789 987654321 998244353 500000004
