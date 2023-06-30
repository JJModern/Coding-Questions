import sys

f = sys.stdin.read().splitlines()

word_dict = {'Y': 'e', 'e': 's', 's': 'Y'}

for curr_str in f[1:]:
    if not set(curr_str).issubset({'Y', 'e', 's'}):
        print("NO")
        continue

    found = True
    for i, char in enumerate(curr_str[1:]):
        if word_dict[curr_str[i]] != char:
            found = False
            break

    if found:
        print("YES")
    else:
        print("NO")
