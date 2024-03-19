import sys
import heapq

f = sys.stdin.read().splitlines()
n, _, cost = list(map(int, f[0].split()))
# O(N)

myheap = []

for i in range(1, n + 1):
    curr_list = list(map(int, f[i].split()))
    heapq.heapify(curr_list)
    heapq.heappush(myheap, (curr_list[0], curr_list))

result = 0
total_cost = 0

# O(N)
done = False
while not done:
    tempheap = []
    while myheap:
        min_cost, sublist = heapq.heappop(myheap)
        if sublist:
            if min_cost + total_cost > cost:
                done = True
                break
            else:
                total_cost += min_cost
                if len(sublist) == 1:
                    done = True
                else:
                    heapq.heappop(sublist)
                    tempheap.append((sublist[0], sublist))
                result += 1
    heapq.heapify(tempheap)
    myheap = tempheap

print(result)
# sort by C (min and max ) differ by 1.