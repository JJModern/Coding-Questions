import copy

# convert
nums = [1, 211, 223]

new_nums = copy.deepcopy(nums)

for num in nums:
    new_nums.append(int(str(num)[::-1]))

# make into a set
new_nums = set(new_nums)

print(len(new_nums))
