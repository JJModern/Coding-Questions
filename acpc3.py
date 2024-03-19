import sys

f = sys.stdin.read().splitlines()
f = [list(map(int, item.split())) for item in f]

nums = f[1]

mysum = sum(nums)

distances = dict()
for num in nums:
    distances[mysum - num] = True

mylist = sorted(list(map(str, distances.keys())))
print(str(len(mylist)))
print(" ".join(mylist))