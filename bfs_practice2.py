import collections


class Solution(object):
    def queue_land(self, grid, queue, row_col_tuple):
        i, j = row_col_tuple
        if i - 1 >= 0:
            queue.append((i - 1, j))
        if j - 1 >= 0:
            queue.append((i, j - 1))
        if i + 1 <= len(grid) - 1:
            queue.append((i + 1, j))
        if j + 1 <= len(grid[0]) - 1:
            queue.append((i, j + 1))

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # 1 land 0 water, 0 water outside grid
        island_count = 0
        visited_set = set()
        queue = collections.deque()
        for i, _ in enumerate(grid):
            for j, element in enumerate(grid[i]):
                # if it is land go ahead, if not finish it up.
                if element == "1":
                    if (i, j) not in visited_set:
                        queue.append((i, j))
                        island_count += 1

                        while len(queue) > 0:
                            row, col = queue.popleft()
                            if grid[row][col] == "1":
                                if (row, col) not in visited_set:
                                    visited_set.add((row, col))
                                    # helper that adds all connecting land to queue
                                    self.queue_land(grid, queue, (row, col))
                            else:
                                visited_set.add((row, col))
                else:
                    visited_set.add((i, j))
        return island_count


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
solution_inst = Solution()
print(solution_inst.numIslands(grid))
