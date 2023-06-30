# [0, 0, 3, 3, 3]
# [3, 0, 0, 3, 3, 0]
#[0, 5, 4, 0, 3, 2, 1]
#[0, 3, 4, 0, 5, 2, 1]
#[4, 0, 0, 1, 3]
lst = [0, 3, 4, 0, 5, 2, 1]

# when only one zero

# reverse the list

# can put lru_cache here.
def max_gain(lst, k):
    first_zero = lst.index(0)
    lst = lst[first_zero:]
    if k == 0:
        return 0
    if k == 1:
        if not lst:
            return 0
        else:
            return max(lst)

    if len(lst) - k == k:
        return sum(lst)
    
    # take one
    # and then recurse
    max_val = 0
    for i, element in enumerate(lst):
        if element != 0:
            # remove last 0
                #get to second last 0

            # control for each try except
            try:
                second_zero = lst.index(0, 1)
                if second_zero < i:
                    max_val = max(max_val,
                          element + max_gain([0] + lst[i + 1:], k - 1))
                else:
                    max_val = max(max_val,
                          element + max_gain(lst[i + 1:], k - 1))
            except:
                # means last zero
                max_val = max(max_val, element)

    return max_val


print(max_gain(lst, 2))
# output
