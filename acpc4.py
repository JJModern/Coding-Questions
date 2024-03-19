import sys

def square_simplify(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        
        exp = exp // 2
        base = (base ** 2) % mod
    return result

f = sys.stdin.read().splitlines()
f = [list(map(int, item.split())) for item in f]
n, m = f[0][0], f[0][1]
first = square_simplify(2, (n + 1), m)
second = square_simplify(2, (max((n - 1), 0)), m)
print((first + second - 1) % m)
# print(((((1 << (n + 1)) % m)+ ((1 << max((n - 1), 0)) - 1) % m) % m ))




# 0 - 2
# 1 - 4
# 2 - 8
# 3 - 16

# max(n - 1, 0)
# commas
# 0 - 0
# 1 - 0
# 2 - 1
# 3 - (n - 1) + cumsum() = 3
# 4 - (n - 1) + cumsum() = 3 + 4 = 7
# 5 - (n - 1) + cumsum() = 4 + 11 = 15
# 6 - (n - 1) + sumsum() = 5 + 26 = 31

# max(int(2 ** (n - 1)), 1) - 1

# exponent
# 0: 0
# 1: 0
# 

# 1 -> -1 the rest become what ever their number - 1

# int(2 ** (n - 1)), 1)

# 1 << max((n - 1), 0)

