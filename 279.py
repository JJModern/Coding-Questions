import collections


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        largest_root = int((n**0.5) // 1)

        return_num = 1

        queue = collections.deque([[largest_root]])

        while queue:
            sum_lst = queue.popleft()

            if sum(sum_lst) == n:
                return len(sum_lst)

            sum_lst.sort(reverse=True)

            for i in range(sum_lst[0], 0, -1):
                temp = sum_lst + [i]
                sum_temp = sum(temp)
                if sum_temp == n:
                    return len(temp)
                elif sum_temp < n:
                    queue.append(temp)


sol = Solution()
print(sol.numSquares(12))
