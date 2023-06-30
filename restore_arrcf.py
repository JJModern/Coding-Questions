import sys

f = sys.stdin.read().splitlines()

# option 1
f = [list(map(int, item.split())) for item in f]
num = f[0][0]

for i in range(1, num + 1):
    sub_lst = f[i * 2]
    return_lst = [str(sub_lst[0])] + ["-1" for _ in sub_lst]
    return_lst[-1] = str(sub_lst[-1])
    return_lst[-2] = str(sub_lst[-1])
    for i, middle_max in enumerate(sub_lst[:len(sub_lst) - 1]):
        right_max = sub_lst[i + 1] 
        if middle_max > right_max:
            # return_lst[i] = middle_max
            return_lst[i + 1] = str(right_max)
        elif middle_max < right_max:
            # return_lst[i] = middle_max
            return_lst[i + 1] = str(middle_max)
            # return_lst[i + 2] = right_max
        else:
            return_lst[i + 1] = str(middle_max)

    print(" ".join(return_lst))

# middle max > second max
    # middle_max[0] is middle_max
# middle < second max
    # right[1] is second max
# middle == second max
    # middle[1] is the max 

# when last element



# 11
# 5
# 3 4 4 5
# 4
# 2 2 1
# 5
# 0 0 0 0
# 6
# 0 3 4 4 3
# 2
# 10
# 4
# 3 3 3
# 5
# 4 2 5 5
# 4
# 3 3 3
# 4
# 2 1 0
# 3
# 4 4
# 6
# 8 1 3 5 10
