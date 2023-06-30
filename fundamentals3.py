# def f(x):
#     x = x + 1

# y = 5

# f(y)
# print(y)

# # When it is a single value, it does not change the value.

# # you can change list in place while iterating it.
# def scale2(lst):
#     for i, item in enumerate(lst):
#         lst[i] = item * 0.5

# nums = [1, 2, 3, 4]
# print(nums)
# scale2(nums)
# print(nums)


lst = [1, 3, 4, 9, 12, 13, 20, 25, 27, 31, 42, 43, 50, 51]


def binary_search(lst, needle):
    # input: lst
    # output: True found, False: not found
    # base case:
    if len(lst) == 0:
        return False

    middle = len(lst) // 2
    # 1-> 0, 2 -> 1 3 -> 1

    # needle is value
    if lst[middle] == needle:
        return True

    # needle is smaller than value
    if lst[middle] > needle:
        return binary_search(lst[:middle], needle)

    # needle is bigger than value
    return binary_search(lst[middle + 1 :], needle)


for i in lst:
    print("This should return True: ", binary_search(lst, i))

print("This can depend")
for i in range(100):
    print(i, binary_search(lst, i))

# Now more efficient binary search


for i in lst:
    print("This should return True: ", binary_search(lst, i))

print("This can depend")
for i in range(100):
    print(i, binary_search(lst, i))
