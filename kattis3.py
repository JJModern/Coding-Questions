import sys

#|f(x) - f(y)|/|x - y| <= L 
f = sys.stdin.read().splitlines()
num = f[0]
f = f[1:]

num_combo = num * (num - 1) / 2
min_lip = float("inf")

for i in range(num_combo):
