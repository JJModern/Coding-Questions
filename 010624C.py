import sys
from functools import lru_cache
sys.setrecursionlimit(10**6)
f = sys.stdin.read().splitlines()
f = [list(map(int, item.split())) for item in f]

@lru_cache(maxsize=10000)
def rec(maxa, minb):
    # print(f"running{a}, {b}")
    # if my_list[a][b]:
    #     return my_list[a][b]

    if maxa > 1:
        # aleft = maxa // 2
        # aright = maxa - aleft
        # result1 = a * b + rec(my_list, aleft, minb) + rec(my_list, aright, minb)
        maxc = max(maxa - 1, minb)
        mind = min(maxa - 1, minb)
        result2 = maxa * minb + rec(minb, 1) + rec(maxc, mind)
        # print(result2)
        # my_list[a][b], my_list[b][a] = result2, result2
        # print(a, b, result2)
        return result2
        # return max(result1, result2)
    else:
        # print(a * b)
        return 1

a, b = f[0][0], f[0][1]
# maxa = max(a, b)
# my_list = [[None for i in range(maxa + 1)] for j in range(maxa + 1)]
# my_list[0][0], my_list[1][1], my_list[0][1], my_list[1][0] = 1, 1, 1, 1
maxa = max(a, b)
minb = min(a, b)
print(rec(maxa, minb))

# test case    
# print(rec(3, 2))