# # Intuition
# Euler Sandwich to Precompute the Maximum Tree Levels

# # Approach
# Euler Tour is like a list sandwich of the root node of a tree surrounding the nodes within that tree.

# tour: you first create a list of sandwiching Euler Tour list
# map_indices: you map the indices of where the starting and ending indices are
# map_prefix_suffix: you calculate the prefix and suffix maximum levels.
# give_answer: easily computes the maximum level when the subtree is removed.

# # Complexity
# - Time complexity:
# O(N)

# Calculating the tour, indices, prefix, and suffix takes O(N). After that, each iteration of query takes O(1), a simple calculation based on indexing pre-computed numbers.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Map (list) node reference, height, other_node_height (if enone, -1)

def tour(euler_tour, node, level):
    if not node:
        return

    euler_tour.append((node.val, level))
    tour(euler_tour, node.left, level + 1)
    tour(euler_tour, node.right, level + 1)
    euler_tour.append((node.val, level))

def map_indices(indices, euler_tour):
    for i, item in enumerate(euler_tour):
        indices[item[0]] = indices.get(item[0], []) + [i]

def map_prefix_suffix(prefix_max, suffix_max, euler_tour):
    max_ind = len(euler_tour) - 1
    for i, (_, level) in enumerate(euler_tour):
        prefix_max[i] = max(prefix_max[i - 1], level)

        _, suffix_level = euler_tour[max_ind - i]
        suffix_max[max_ind - i] = max(suffix_max[max_ind - i + 1], suffix_level)

def give_answer(queries, indices, prefix_max, suffix_max):
    return_answer = []
    for query in queries:
        start, end = indices[query]
        # this includes possibility of list spillover
        return_answer += [max(prefix_max[start - 1], suffix_max[end + 1])]
    return return_answer

class Solution(object):
    def treeQueries(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[int]
        """
        euler_tour = []
        indices = {}    
        
        tour(euler_tour, root, 0)

        map_indices(indices, euler_tour)

        prefix_max = [0 for i in range(len(euler_tour) + 1)]
        suffix_max = [0 for i in range(len(euler_tour) + 1)]

        map_prefix_suffix(prefix_max, suffix_max, euler_tour)

        return give_answer(queries, indices, prefix_max, suffix_max)

# class Solution(object):
#     def treeQueries(self, root, queries):
#         """
#         :type root: Optional[TreeNode]
#         :type queries: List[int]
#         :rtype: List[int]
#         """
#         node_map = {}
#         total_height = create_map(root, node_map)

#         return_list = []
#         for query in queries:
#             node, height, neighbor_height = node_map[query]
            
            
# def create_map(root, node_map):
#     # returns max height
#     if root is None:
#         return -1
#     else:

#         # set root height
#         left_height = create_map(root.left, node_map)
#         right_height = create_map(root.right, node_map)
#         max_height = max(left_height, right_height) + 1
#         node_map[root.val] = [root, max_height, -1]

#         # set neighbor height for left and right
#         if None not in (root.left, root.right):
#             node_map[root.left.val][2] = right_height
#             node_map[root.right.val][2] = left_height

#         return max_height


# def get_height(count_so_far, root):
#     if root is None:
#         return count_so_far - 1

#     if root.left is None and root.right is None:
#         return count_so_far
    
#     return max(get_height(count_so_far + 1, root.left), get_height(count_so_far + 1, root.right))


# def copy_tree(root):
#     if root is None:
#         return None
#     returnNode = TreeNode(val = root.val)
#     returnNode.left = copy_tree(root.left)
#     returnNode.right = copy_tree(root.right)

#     return returnNode

# def remove_node(root, value):
#     if root is None:
#         return
#     elif root.left is not None and root.left.val == value:
#         root.left = None
#     elif root.right is not None and root.right.val == value:
#         root.right = None
#     else:
#         remove_node(root.left, value)
#         remove_node(root.right, value)

        # count the height of original tree


        # Simplified version
        # just count it again after removing

        # Optimized Version
        # keep track of height at removal 
            #(and height of removed tree)

            # calculate new height

# class Solution(object):
#     def treeQueries(self, root, queries):
#         """
#         :type root: Optional[TreeNode]
#         :type queries: List[int]
#         :rtype: List[int]
#         """

#         return_list = []
#         for query in queries:
#             # copy original tree
#             curr_root = copy_tree(root)
#             if curr_root.val == query:
#                 return_list.append(0)
#             else:
#                 remove_node(curr_root, query)
#                 return_list.append(get_height(0, curr_root))
            
#         return return_list

