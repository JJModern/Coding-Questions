import math

nums = [1, 3, 5, 2, 7, 5]
minK = 1
maxK = 5

num_len = len(nums)
count = 0
for i in range(num_len):
    if nums[i] > maxK or nums[i] < minK:
        continue
    for j in range(i, num_len):
        if nums[j] > maxK or nums[j] < minK:
            break
        if max(nums[i : j + 1]) == maxK and min(nums[i : j + 1]) == minK:
            count += 1

print(count)
