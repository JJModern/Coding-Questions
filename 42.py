"""

# Intuition
Pre-calculate maximum height of left and right. Subtract current height from the minimum of the maximum heights because limiting agent of water is minimum of left or right wall.

# Approach
First brute force approach O(N^2):

- Calculate the maximum height of the bars starting from left and right of each bar.
- Find the minimum of these two maximum heights.
- Subtract the current bar's height from this minimum height to calculate the amount of water that the current bar can trap. This is because the bar also takes up space.
- Add up all these sums

Second Pre-computed left_max and right_max lists O(N):

This takes two loops. While you could calculate the lists in two for loops, this is an optimized version that calclulates the maximum height in one loop rather than two. 

- Pre-calculate the maximum height from left and right.
- Then, iterate through height list, doing same calculation.


Third Optimized One Pass O(N):

- This takes one iteration rather than two.
- Pointers start on left and right ends
- Update maximum heights for left and right
- The smaller maximum value side gets index and water updated
    This is because the smaller value is the limiting agent for holding water. As the maximum value never decreases, this is, in effect, the same as comparing the two lists of maximum values in two loops. 
- The updating side goes through the same calculation as above 
    total_water += max_value - height[index]

# Complexity
- Time complexity:
O(N)

- Space complexity:
O(1)
While the previous versions would be O(N) because of the two lists, this now only stores the current 2 maximum values. 
"""

# Third Optimized One Pass O(N) Code


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

