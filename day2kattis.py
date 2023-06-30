import sys
import copy

# learn how to map things


def infect(lst, row, col):
    new_lst = copy.deepcopy(lst)
    for i in range(row):
        for j in range(col):
            if lst[i][j] == 1:
                for k in range(max(0, i - 1), min(i + 1, row - 1) + 1):
                    new_lst[k][j] = 1

                for k in range(max(0, j - 1), min(j + 1, col - 1) + 1):
                    new_lst[i][k] = 1

    return new_lst


f = sys.stdin.read().split()
row = int(f[0])
col = int(f[1])
lst = [[0 for j in range(col)] for i in range(row)]

# create matrix of row and columns
# put 1 as occupied, 0 as unoccupied
f = f[3:]

for i in range(0, len(f), 2):
    lst[int(f[i]) - 1][int(f[i + 1]) - 1] = 1

count = 0

while True:
    # repeat for each point
    new_lst = []
    # function that finds the neighboring places
    # and occupies for 1 spot.
    new_lst = infect(lst, row, col)

    count += 1
    # at the end when it doesn't change, break loop
    if new_lst == lst:
        break
    lst = new_lst

print(count)
