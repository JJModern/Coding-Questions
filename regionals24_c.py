import sys

f = sys.stdin.read().splitlines()
f = [list(map(str, item.split())) for item in f]

myword = f[0][0]
found = True
if len(myword) > 10:
    found = False

else:
    for i in range(1, len(myword) + 1):
        if myword[i - 1] != str(i):
            found = False

print(len(myword) if found else -1)
