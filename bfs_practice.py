# bfs template.

from queue import Queue


def bfs(root, target):
    queue_lst = Queue()
    queue_lst.put(root)
    visited_set = set([root])
    step = 0

    while len(queue_lst) > 0:
        queue_size = queue_lst.qsize()

        for i in range(queue_size):
            curr_node = queue_lst.get()
            if curr_node == target:
                return step
            for child_node in curr_node.children:
                if child_node not in visited_set:
                    visited_set.add(child_node)
                    queue_lst.put(child_node)

        step += 1

    return -1
