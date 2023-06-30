def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    str1 = s

    right_index = 0
    while right_index != -1:
        right_index = str1.find("]")
        if right_index == -1:
            break
        left_index = right_index - str1[right_index::-1].find("[")
        k_left_index = left_index

        k_num = 0
        for i in range(3):
            char = str1[left_index - 1 - i]
            if char.isnumeric():
                k_left_index = left_index - 1 - i
                k_num += int(char) * (10**i)
            else:
                break

        str1 = (
            str1[:k_left_index]
            + (str1[left_index + 1 : right_index] * k_num)
            + str1[right_index + 1 :]
        )
    return str1


print(decodeString("3[a]2[bc]"))
