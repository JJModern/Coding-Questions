import sys
import pdb

f = sys.stdin.read().splitlines()

num = int(f[0])

return_lst = []

for i in range(1, num + 1):
    k = int(f[i * 2 - 1].split()[1])
    curr_str = f[i * 2]
    count_dict = dict()

    for char in curr_str:
        count_dict[char] = count_dict.get(char, 0) + 1

    key_set = {item.lower() for item in count_dict.keys()}

    # print(count_dict)
    matches_so_far = 0
    potential_matches = 0
    for key in key_set:
        upper_key = key.upper()
        # both not in - no need to account for

        # only one in
        if upper_key not in count_dict or key not in count_dict:
            potential_matches += (
                count_dict.get(key, 0) + count_dict.get(upper_key, 0)
            ) // 2
        else:
            try:
                upper_count = count_dict[upper_key]
                normal_count = count_dict[key]
            except:
                pdb.set_trace()
            matches_so_far += min(upper_count, normal_count)
            potential_matches += abs(upper_count - normal_count) // 2

    return_lst += [str(matches_so_far + min(potential_matches, k))]

print("""\n""".join(return_lst))


# 5
# 11 2
# aAaaBACacbE
# 2 2
# ab
# 4 1
# aaBB
# 6 0
# abBAcC
# 5 3
# cbccb
