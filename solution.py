import random

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        self.sum = sum(self.w)

    def pickIndex(self):
        """
        :rtype: int
        """
        sum_so_far = 0
        temp_w = self.w[:]
        lst_len = len(self.w)

        for i in range(lst_len):
            sum_so_far += temp_w[i]
            temp_w[i] = sum_so_far

        ran_num = random.randint(1, temp

        _w[-1])

        left_bound = 0
        right_bound = lst_len - 1

        for _ in temp_w:
            mid_idx = (right_bound + left_bound) // 2

            if (left_bound == right_bound or
               mid_idx == 0):
                return mid_idx
            #found
            if (temp_w[mid_idx - 1] < ran_num and ran_num <= temp_w[mid_idx]):
                return mid_idx
            #is on the left
            if(ran_num <= temp_w[mid_idx]):
                right_bound = mid_idx - 1
            else:
                left_bound = mid_idx + 1

#         for i, item in enumerate(temp_w):
#             if ran_num <= item:
#                 return i

        #return self.binary_search(temp_w, ran_num)

    # def binary_search(self, lst, needle, head_index = 0):
    #     """
    #         return index
    #     """
    #     if len(lst) == 1:
    #          return 0
    #     middle_idx = len(lst)//2
    #     if (lst[middle_idx] > needle):
    #         if middle_idx == len(lst) - 1:
    #             return head_index + middle_idx
    #         elif lst[middle_idx + 1] <= needle:
    #             return head_index + middle_idx + 1
    #         else:
    #             return self.binary_search(lst[middle_idx + 1:], needle, head_index + middle_idx + 1)
    #     else:
    #         return self.binary_search(lst[:middle_idx], needle, head_index)



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

#w[i] / sum(w)
#cumulative list
#random.uniform()

