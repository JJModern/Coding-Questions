# print(5 // 1)
# print(50 // 10)
# print(52 // 10)
# print(54 // 10)
# print(541 // 100)

# number = 5621
# i = 3
# result = number % (10 ** (i + 1)) // 10 ** i
# print(result)

import collections


def openLock(deadends, target):
    """
    :type deadends: List[str]
    :type target: str
    :rtype: int
    """
    if "0000" in deadends or target in deadends:
        return -1

    deadends = set(deadends)
    queue = collections.deque()
    queue.append((target, 0))
    seen = set()

    while queue:
        number, depth = queue.popleft()

        if number == "0000":
            return depth

        if number in deadends:
            continue

        seen.add(number)

        for i in range(4):
            number_str = int(number[3 - i])

            lower_num = number[: 3 - i] + str((number_str + 1) % 10) + number[4 - i :]
            higher_num = number[: 3 - i] + str((number_str - 1) % 10) + number[4 - i :]
            if lower_num not in seen and lower_num not in deadends:
                queue.append((lower_num, depth + 1))
                seen.add(lower_num)
            if higher_num not in seen and higher_num not in deadends:
                queue.append((higher_num, depth + 1))
                seen.add(higher_num)
    return -1


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
print(openLock(deadends, target))
