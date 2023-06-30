def findTargetSumWays(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    sum_combos = {-nums[0]: 1}
    sum_combos[nums[0]] = sum_combos.get(nums[0], 0) + 1

    for num in nums[1:]:
        new_combo = dict()
        for sum_combo, count in sum_combos.items():
            new_combo[sum_combo + num] = new_combo.get(sum_combo + num, 0) + count
            new_combo[sum_combo - num] = new_combo.get(sum_combo - num, 0) + count
        sum_combos = new_combo

    return sum_combos.get(target, 0)


nums = [0, 0, 0, 0, 0, 0, 0, 0, 1]
target = 1

print(findTargetSumWays(nums, target))
