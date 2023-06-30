from solution import *

solution_instance = Solution([3, 14, 1, 7])


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def creatBTree(data, index):
    pNode = None
    if index < len(data):
        if data[index] == None:
            return
        pNode = TreeNode(data[index])
        pNode.left = creatBTree(data, 2 * index + 1)  # [1, 3, 7, 15, ...]
        pNode.right = creatBTree(data, 2 * index + 2)  # [2, 5, 12, 25, ...]
    return pNode


lst = [-2, 1]
root = creatBTree(lst, 0)

# solution_instance.TRY_METHOD here
return_str = ""
for i in range(100):
    return_str += str(solution_instance.pickIndex())
print(return_str)
