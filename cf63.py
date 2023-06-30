import sys
import collections

f = sys.stdin.read().splitlines()
total = int(f[0])
total %= 3 * 5 * 7
stack = collections.deque([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
visited = set()
dic = {0: 3, 1: 5, 2: 7}

return_value = -1

while stack:
    curr_path = stack.pop()
    curr_total = curr_path[0] * 3 + curr_path[1] * 5 + curr_path[2] * 7
    if tuple(curr_path) not in visited:
        visited.add(tuple(curr_path))
        for i in range(3):
            new_path = curr_path.copy()
            new_path[i] += 1
            if curr_total + dic[i] < total:
                stack.append(new_path)
            elif curr_total + dic[i] == total:
                # END
                stack = []
                return_value = new_path
                break
            else:
                visited.add(tuple(new_path))
try:
    if isinstance(return_value, list):
        return_value = " ".join(return_value)
except:
    pass

print(return_value)
