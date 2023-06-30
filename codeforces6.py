# 7 diff ways
import sys

f = sys.stdin.read().splitlines()
f = [list(map(int, item.split())) for item in f]

total_money = f[0][0]

prices = [f[1][0], f[2][0], f[3][0]]
prices.sort()

cost_so_far = 0
count = 0
while cost_so_far < total_money:
    for price in prices:
        cost_so_far += price

        if cost_so_far == total_money:
            count += 1
            break
        elif cost_so_far > total_money:
            break
        else:
            count += 1

print(count)
