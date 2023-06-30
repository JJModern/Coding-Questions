import heapq


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # have to consider width too

        # brute force

        # sliding window - move one with shorter height
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            width = r - l
            max_area = max(max_area, width * min(height[r], height[l]))

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_area


# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.
