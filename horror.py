# sort the numbers
# pick one
# delete all smaller on the other one.
import sys

f = sys.stdin.read().splitlines()
f1 = list(map(int, f[0].split()))[1:]
f2 = list(map(int, f[1].split()))[1:]
f1.sort(reverse=True)
f2.sort(reverse=True)

print(f1, f2)

total1 = 0
f1_turn = True
while True:
    if len(f1) == 0 or len(f2) == 0:
        break
    if f1_turn:
        num = f1.pop()
        total1 += 1
        find_lst = [i for i, item in enumerate(f2) if item < num]
        find_lst.sort(reverse=True)
        f2 = f2[find_lst[0] :]
        f1_turn = False
    else:
        num = f2.pop()
        total1 += 1
        find_lst = [i for i, item in enumerate(f1) if item < num]
        find_lst.sort(reverse=True)
        f1 = f1[find_lst[0] :]
        f1_turn = True

f1 = list(map(int, f[0].split()))[1:]
f2 = list(map(int, f[1].split()))[1:]
f1.sort(reverse=True)
f2.sort(reverse=True)
print(f1, f2)

total2 = 0
f1_turn = False
while True:
    if len(f1) == 0 or len(f2) == 0:
        break
    if f1_turn:
        num = f1.pop()
        total2 += 1
        find_lst = [i for i, item in enumerate(f2) if item < num]
        find_lst.sort(reverse=True)
        f2 = f2[find_lst[0] :]
        f1_turn = False
    else:
        num = f2.pop()
        total2 += 1
        find_lst = [i for i, item in enumerate(f1) if item < num]
        find_lst.sort(reverse=True)
        f1 = f1[find_lst[0] :]
        f1_turn = True

print(total1, total2)
