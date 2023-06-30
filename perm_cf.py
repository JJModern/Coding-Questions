import sys
from collections import Counter

f = sys.stdin.read().splitlines()
f = [list(map(int, item.split())) for item in f]
num = f[0][0]

for i in range(1, num + 1):
    curr_lst = f[i * 2]
    missing = f[i * 2 - 1][1]

    if len(set(curr_lst)) != len(curr_lst):
        print("NO")
        continue

    # check if more than 1
    max_num = max(curr_lst)

    # 1 through max
    result = missing - (max_num * (max_num + 1) / 2 - sum(curr_lst))

    found = False
    while result >= 0:
        if result == 0:
            found = True
            break
        max_num += 1
        result -= max_num

    if found:
        print("YES")
    else:
        print("NO")



    

    

    