from functools import lru_cache
import sys

# f = sys.stdin.read().splitlines()
# f = [int(item) for item in f]

# nums = f[1: ]
nums = [0, 1, 2, 3, 4, 3, 2, 1, 0, 7, 8, 9]

count_prefix = [dict()]
count_dict = dict()
global is_zero
is_zero = False

for num in nums:
    # can improve with default dict
    count_dict[num] = count_dict.get(num, 0) + 1

    # improve speed of accessing max with heap later.
    count_prefix.append(count_dict.copy())


def breakup(left, right, target):
    islands = []
    for i in range(left, right + 1):
        if nums[i] != target:
            if i == left or nums[i - 1] == target:
                islands.append(i)
            if i == right or nums[i + 1] == target:
                islands.append(i)

    return islands

@lru_cache
def dp(left, right):
    new_dict = dict()
    left_dict = count_prefix[left]
    right_dict = count_prefix[right + 1]

    if right - left == 0:
        return 1
    elif right - left == 1:
        return 2 if nums[right] != nums[left] else 1

    for key in right_dict:
        new_dict[key] = right_dict[key] - left_dict.get(key, 0)

    sorted_list = sorted(new_dict.items(), key= lambda x: x[1], reverse= True)
    max_count = sorted_list[0][1]
    max_result = float("inf")

    for tup in sorted_list:
        if tup[1] != max_count:
            break
        islands = breakup(left, right, tup[0])
        total = 0
        if tup[0] == 0:
            is_zero = True
        for i in range(len(islands) // 2):
            total += dp(islands[i * 2], islands[i * 2 + 1])

        is_zero = False

        max_result = min(max_result, total + 1)

    return max_result
    

islands = breakup(0, len(nums) - 1, 0)
total = 0

if len(islands) == 0:
    print(0)
else:
    is_zero = True
    for i in range(len(islands) // 2):
        total += dp(islands[i * 2], islands[i * 2 + 1])

    is_zero = False

    print(min(total, dp(0, len(nums) - 1)))