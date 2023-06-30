# f = sys.stdin.read().splitlines()
# f = [list(map(int, item.split())) for item in f]

# new = [list(map(int, item.split())) for item in f]
# print(new)
# f = list(map(int, sys.stdin.read().splitlines()))

import sys

f = sys.stdin.read().splitlines()
# f = [list(map(int, item.split())) for item in f]
storage = {}

for item in f[1:]:
    if item == "":
        break
    value, key = tuple(map(int, item.split(" ")))
    if key <= int(f[0].split()[1]):
        # print("key and value", key, value)
        storage[key] = storage.get(key, []) + [value]

sum = 0
storage = list(storage.items())
storage.sort()
for key, item in storage:
    item.sort(reverse=True)
    sum += item[0]

print(sum)
