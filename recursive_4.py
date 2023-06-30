def binary_efficient(lst, lb, ub, needle):
    # input, lst, lb: start with 0 and until lb == ub ub: start with n - 1,
    # output: True (found), False (not found)

    # base case
    if ub < lb:
        return False

    middle = (lb + ub) // 2
    # if found
    if lst[middle] == needle:
        return True

    # if needle is smaller than value
    if needle < lst[middle]:
        return binary_efficient(lst, lb, middle - 1, needle)

    # if needle is larger than value
    return binary_efficient(lst, middle + 1, ub, needle)


lst = [1, 3, 4, 9, 12, 13, 20, 25, 27, 31, 42, 43, 50, 51]

for i in lst:
    print("This should return True: ", binary_efficient(lst, 0, len(lst) - 1, i))

print("This can depend")
for i in range(100):
    print(i, binary_efficient(lst, 0, len(lst) - 1, i))
