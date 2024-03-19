import sys

# left inclusive, right not inclusive, zero indexed
class SegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1

        return self._func(res_left, res_right)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)

f = sys.stdin.read().splitlines()
f = [list(map(int, item.split())) for item in f]

heights = f[1]
costs = f[2]
costsum = []
maxheight = SegmentTree(heights)

# O(N)
max_ind = {}
for i, height in enumerate(heights):
    max_ind[height] = max_ind.get(height, []) + [i]


total = 0
for cost in costs:
    total += cost
    costsum.append(total)

def compare(indices, left, right, index):
    # (False, leftcost) if leftcost is larger, (True, rightcost) if rightcost is larger.
    if left == 0:
        if indices[index] == 0:
            leftcost = 0
        else:
            leftcost = costsum[indices[index] - 1]
        # vs
        rightcost = costsum[right] - costsum[indices[index]]
    else:
        leftcost = costsum[indices[index] - 1] - costsum[left - 1]
        # vs
        rightcost = costsum[right] - costsum[indices[index]]
    # print("leftcost, rightcost: ", leftcost, rightcost)
    if leftcost >= rightcost:
        return (False, leftcost)
    else:
        return (True, rightcost)

def rec(left, right):
    # print(left, right)
    currmax = maxheight.query(left, right + 1)
    indices = max_ind[currmax]
    
    if left == right:
        # print("case1")
        return costs[left]
    if left > right:
        # print("case2")
        return 0

    if len(indices) <= 1:
        rightlarger, cost = compare(indices, left, right, 0)

        if rightlarger:
            # print("case3")
            return costs[indices[0]] + rec(left, indices[0] - 1)
        else:
            # print("case4", cost)
            return costs[indices[0]] + rec(indices[0] + 1, right)
    else:
        indices.sort()

        leftBool, leftCost = compare(indices, left, right, 0)
        rightBool, rightCost = compare(indices, left, right, -1)

        if leftCost >= rightCost:
            if leftBool:
                # right is larger
                # print("case5")
                return costs[indices[0]] + rec(left, indices[0] - 1)
            else:
                # print("case6")
                return costs[indices[0]] + rec(indices[0] + 1, right)
        else: 
            if rightBool: 
                return costs[indices[-1]] + rec(left, indices[0] - 1)
            else:
                return costs[indices[-1]] + rec(indices[0] + 1, right)

    # get max cost sum 

# print(costsum)    
print(rec(0, len(heights) - 1))

# # print(maxheight.query(2, 3))
# # print(max_ind)



    