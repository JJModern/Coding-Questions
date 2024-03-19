ret = True
nimdig = input()

for i in range(3):
    arr = input().split()
    if "7" not in arr:
        ret = False

print("777" if ret else "0")