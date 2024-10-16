import sys

f = sys.stdin.read().splitlines()

# option 1
f = [list(map(int, item.split())) for item in f]

# for each lottery
n = f[0][0]

threshold = 2 * n

mydict = {}

for sublist in f[1:]:
    for num in sublist:
        mydict[num] = mydict.get(num, 0) + 1


returnlist = []
for key, count in mydict.items():
    if count > threshold:
        returnlist.append(key)

returnlist.sort()

if returnlist:
    print(" ".join(map(str, returnlist)))
else:
    print("-1")
    
