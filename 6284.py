def isItPossible(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: bool
    """
    # count
    count1 = dict()
    count2 = dict()
    for item1 in word1:
        count1[item1] = count1.get(item1, 0) + 1

    for item2 in word2:
        count2[item2] = count2.get(item2, 0) + 1

    print(count1)
    print(count2)

    count_dif = len(count1) - len(count2)
    key_set = set(count1.keys())
    key_set = key_set.union(set(count2.keys()))

    count1_val = count1.values()
    count2_val = count2.values()

    # if count difference is larger than 2, return false

    if abs(count_dif) > 2:
        return False

    if count_dif == 0:
        if len(key_set) < len(count1) + len(count2):
            return False
        return True

    # find keys with 1 count
    one_count_keys1 = set()
    for key, count in count1.items():
        if count == 1:
            one_count_keys1.add(key)

    one_count_keys2 = set()
    for key, count in count2.items():
        if count == 1:
            one_count_keys2.add(key)

    if abs(count_dif) == 1:
        selection = [
            (set(count1.keys()), one_count_keys1),
            (set(count2.keys()), one_count_keys2),
        ]
        index = 0
        if count_dif == -1:
            index = 1

        for key in selection[index][1]:
            if key in selection[index - 1][0]:
                for key2 in selection[index - 1][0].difference(selection[index - 1][1]):
                    if key != key2 and key2 in selection[index][0]:
                        return True

        true_first = False
        for key in selection[index][0].difference(selection[index][1]):
            true_first = true_first or key not in selection[index - 1][0]

        true_second = False
        for key in selection[index - 1][0].difference(selection[index - 1][1]):
            true_second = true_second or key in selection[index][0]

        if true_first and true_second:
            return True

    elif len(one_count_keys1) > 0 and len(one_count_keys2) > 0:
        # find if possible
        # key1 in count2
        non_unique1 = []
        for key in one_count_keys1:
            if key in count2:
                non_unique1 += [key]

        non_unique2 = []
        for key in one_count_keys2:
            if key in count1:
                non_unique2 += [key]

        if len(non_unique1) == 1 and len(non_unique2) == 1:
            if non_unique1 == non_unique2:
                return False

        if len(non_unique1) >= 1 and len(non_unique1) >= 1:
            return True

    return False


word1 = "a"
word2 = "bb"
print(isItPossible(word1, word2))
