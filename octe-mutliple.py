import sys

f = sys.stdin.read().splitlines()

# option 1
f = [item.split() for item in f]

# for each lottery
n = int(f[0][0])

threshold = 2 * n
returnset = set()

mydict = {}

for i in range(n):
    # 1:10, 11: 20
    for sublist in f[i * 10 : (i + 1) * 10 + 1]:
        for num in sublist:
            mydict[num] = mydict.get(num, 0) + 1

    for key, count in mydict.items():
        if count > threshold:
            returnset.add(key)

returnlist = sorted(list(returnset))

if returnlist:
    print(" ".join(returnlist))
else:
    print("-1")






