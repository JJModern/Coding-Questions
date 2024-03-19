temp = input().split()
n = int(temp[0])
s = int(temp[1])

for i in range(n):
    r = input().split()
    if s>= int(r[0]) and s <= int(r[1]):
        s += 1
print(s)