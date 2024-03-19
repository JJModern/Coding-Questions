import sys

# Read input
f = sys.stdin.read().splitlines()
f = [list(map(int, item.split())) for item in f]

a, b = f[0][0], f[0][1]
maxa = max(a, b)
minb = min(a, b)

# Initialize a 2D array (dp_table) to store computed values
dp_table = [[0 for _ in range(minb + 1)] for _ in range(maxa + 1)]

# Base cases
dp_table[0][0] = 1
dp_table[1][1] = 1
dp_table[0][1] = 1
dp_table[1][0] = 1

# Build the solution bottom-up
for i in range(2, maxa + 1):
    for j in range(1, minb + 1):
        # The computation logic
        maxc = max(i, j)
        mind = min(i, j)
        dp_table[i][j] = i * j + dp_table[1][mind] + dp_table[maxc - 1][mind]

# The answer is now in dp_table[maxa][minb]
print(dp_table[maxa][minb])