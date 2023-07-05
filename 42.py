# First Approach

# Ex 1)
# height
# 0 1 0 2 1 0 1 3 2 1 2 1

# left_max list 
# 0 1 1 2 2 2 2 3 3 3 3 3 

# right_max list
# 3 3 3 3 3 3 3 3 2 2 2 1 

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # pre-compute optimized version
        max_ind = len(height) - 1
        left_max, right_max = [], []

        curr_left_max, curr_right_max = 0, 0
        for i, curr in enumerate(height):
            curr_left_max = max(curr, curr_left_max)
            left_max.append(curr_left_max)

            curr_right_max = max(height[max_ind - i], curr_right_max)
            right_max = [curr_right_max] + right_max


        total_water = 0
        for i, curr_height in enumerate(height):
            # water only held for minimum height of left and right
            min_wall = min(left_max[i], right_max[i])

            # you subtract current height because wall takes up space
            total_water += min_wall - curr_height

        return total_water

# Faster (one pass)
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left_ind, right_ind = 0, len(height) - 1
        left_max, right_max = 0, 0
        total_water = 0

        while left_ind <= right_ind:
            left_max = max(height[left_ind], left_max)
            right_max = max(height[right_ind], right_max)

            if left_max <= right_max:
                total_water += left_max - height[left_ind]
                left_ind += 1

            else:
                total_water += right_max - height[right_ind]
                right_ind -= 1

        return total_water

