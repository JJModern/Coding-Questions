import sys

f = sys.stdin.read().splitlines()
n = int(f[0].split()[0])

names = f[1:n + 1]
initials = f[n+1: ]

mydict = dict()

for name in names:
    currname = name.upper().split()
    initial = currname[0][0] + currname[1][0]
    mydict[initial] = mydict.get(initial, []) + [name]

for initial in initials:
    result = mydict.get(initial, [])

    if len(result) == 0:
        print("nobody")
    elif len(result) > 1:
        print("ambiguous")
    else:
        print(result[0])

# line intersection. do it later.