import sys

f = sys.stdin.read().splitlines()
f = [item.split() for item in f]

for i in range(1, int(f[0][0]) + 1):
    count_dict = {}
    for num in list(f[2 * i][0]):
        count_dict[num] = count_dict.get(num, 0) + 1
    
    total = 0
    m = int(f[(2 * i) - 1][1])

    total += (7 - len(count_dict)) * m 

    # print("m", m, "count len", len(count_dict),"intermediate: ", total)

    for value in count_dict.values():
        total += max(0, m - value)
    print(total)