import sys

f = sys.stdin.read().splitlines()
n = int(f[0])
grid = [list(item) for item in f[1:]]

queue = []

for row in range(n):
    for col in range(n):
        if grid[row][col] == ".":
            queue.append((row, col))

def inc_win_check(row_cols):
    row, col = row_cols
    if grid[row][col] == "O":
        return False

    row_win = True
    for new_col in range(n):
        if grid[row][new_col] != "X":
            row_win = False
            break
    if row_win:
        return True

    col_win = True
    for new_row in range(n):
        if grid[new_row][col] != "X":
            col_win = False
            break
    if col_win:
        return True

    if row != col and n - 1 - col != row:
        return False

    downright  = True
    upright = True
    for i in range(n):
        if grid[i][i] != "X":
            downright = False
        if grid[n - 1 - i][i] != "X":
            upright = False

    return downright or upright

# O(- 18 max checks)
def check_win():

    for row in range(n):
        row_win = True
        for col in range(n):
            if grid[row][col] != "X":
                row_win = False
                break
        if row_win:
            return True

    for col in range(n):
        col_win = True
        for row in range(n):
            if grid[row][col] != "X":
                col_win = False
                break
        if col_win:
            return True

    downright  = True
    upright = True
    for i in range(n):
        if grid[i][i] != "X":
            downright = False
        if grid[n - 1 - i][i] != "X":
            upright = False

    return downright or upright
# can optimize curr_grid and curr_queue send in. 

def dfs(row_cols, dont_check = False):
    # print(grid)
    if not dont_check and inc_win_check(row_cols):
        return 1 << len(queue)
    else:
        if not queue:
            return 0
        row, col = queue.pop()

        grid[row][col] = "X"
        xtotal = dfs(row_cols = (row, col))

        grid[row][col] = "O"
        ototal = dfs(row_cols = (row, col), dont_check = True)

        grid[row][col] = "."
        queue.append((row, col))
        # print("ototal, xtotal", ototal, xtotal)
        return ototal + xtotal

if not queue and check_win():
    print("1")
else:
    print(dfs(row_cols= (0, 0), dont_check = True))