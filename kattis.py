import sys

f = sys.stdin.read().splitlines()[1:]

times = 0
for i in range(len(f)):
    if f[i] == "O":
        times += 2 ** (len(f) - 1 - i)

print(times)
