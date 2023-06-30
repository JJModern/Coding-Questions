"""
    You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

You want to share the chocolate with your k friends so you start cutting the chocolate bar into k + 1 pieces using k cuts, each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

 

Example 1:

Input: sweetness = [1,2,3,4,5,6,7,8,9], k = 5
Output: 6
Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]
Example 2:

Input: sweetness = [5,6,7,8,9,1,2,3,4], k = 8
Output: 1
Explanation: There is only one way to cut the bar into 9 pieces.
"""


class Solution(object):
    def maximizeSweetness(self, sweetness, k):
        """
        :type sweetness: List[int]
        :type k: int
        :rtype: int
        """
        l, r = 1, sum(sweetness) // (k + 1)
        while l < r:
            m = (l + r + 1) // 2
            slices, total = 1, 0
            for s in sweetness:
                total += s
                if total >= m:
                    total = 0
                    slices += 1
            if slices > k + 1:
                l = m
            else:
                r = m - 1
        return l

        # wrong approach that I optimized from.
        # # only one way of cutting it
        # if k == len(sweetness) - 1:
        #     return min(sweetness)

        # l = 1
        # r = sum(sweetness) // k + 1
        # m = (l + r) // 2
        # global_max = float("-inf")

        # #edge case of when m is same as l or r
        # while l < r:
        #     print("M value: ", m)
        #     # one loop dividing it
        #     min_num = float("inf")
        #     curr_total = 0
        #     slice_num = 0
        #     for num in sweetness:
        #         curr_total += num
        #         if curr_total >= m:
        #             min_num = min(min_num, curr_total)
        #             curr_total = 0
        #             slice_num += 1

        #     # end case when it does not exceed needed m
        #     if curr_total != 0:
        #         slice_num += 1
        #         min_num = min(min_num, curr_total)

        #     if slice_num == k:
        #         # min number check
        #         print("Min number is ", min_num)
        #         global_max = max(global_max, min_num)
        #         r = m - 1
        #     else:
        #         if slice_num < k:
        #             r = m - 1
        #         else:
        #         # elif slice_num > k:
        #             l = m
        #     temp_m = m
        #     m = (l + r) // 2

        #     if temp_m == m:
        #         break

        # return global_max
