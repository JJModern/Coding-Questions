import collections


def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """

    stack = collections.deque([root])

    visited = set()
    return_lst = []

    while stack:
        curr_node = stack.pop()

        if curr_node is not None and curr_node not in visited:
            if (curr_node.right is None and curr_node.left is None) or (
                curr_node.right in visited and curr_node.left in visited
            ):
                visited.add(curr_node)
                return_lst += [curr_node]

            else:
                stack.extend([curr_node.right, curr_node, curr_node.left])

    return return_lst


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)

root.right = two
two.left = three


inorderTraversal(root)
