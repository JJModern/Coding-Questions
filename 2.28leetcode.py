import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        p_node, p_path = self.traverse(root, p)
        q_node, q_path = self.traverse(root, q)

        return 0

    def traverse(self, root, val1):
        if not root:
            return None
        curr = root
        path = [root]
        while curr:
            if val1 < root.val:
                path += [curr]
                curr = curr.left

            elif val1 > root.val:
                path += [curr]
                curr = curr.right
            else:
                return (curr, path)

    def find_node(self, head, val1, val2):
        # dfs
        stack = collections.deque([(head, [head])])
        return_1, return_2 = None, None

        while stack:
            curr_node, path_lst = stack.pop()
            if curr_node.val == val1:
                return_1 = (curr_node, path_lst)
            if curr_node.val == val2:
                return_2 = (curr_node, path_lst)

            if return_1 and return_2:
                return (return_1, return_2)

            for node in [curr_node.left, curr_node.right]:
                if node:
                    stack.append((node, path_lst + [node]))


# https://leetcode.com/problems/maximum-depth-of-binary-tree/


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        max_num = 0
        for child in [root.left, root.right]:
            if child:
                max_num = max(self.maxDepth(child), max_num)

        return max_num


# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
