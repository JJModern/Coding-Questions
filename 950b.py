import sys

f = sys.stdin.read().splitlines()
f = [list(map(int, item.split())) for item in f]

for i in range(1, f[0][0] + 1): 
    n, f, k = f[2 * i - 1]
    mylist = f[2 * i]
    myfav = mylist[f - 1]
    mylist.sort(reverse=True)
    if mylist[k] < myfav:
        print("YES")
    else:
        # if left or right is same, then maybe

        # no left
        if len(mylist) <= k:

        # no right

