import sys

f = sys.stdin.read().splitlines()
# when there non characters in there
# when one of the characters are missing
num = int(f[0])
order_dict = {"m": "e", "e": "o", "o": "w", "w": "w"}
return_str = """"""

for i in range(1, num + 1):
    curr_str = f[i * 2]
    curr_str = curr_str.lower()
    prev_char = curr_str[0]
    found = True
    all_chars = set()
    for curr_char in curr_str:
        should_be_next = order_dict.get(prev_char, False)
        all_chars.add(curr_char)
        if not should_be_next:
            found = False
            break
        if prev_char != curr_char and should_be_next != curr_char:
            found = False
            break
        prev_char = curr_char
    if found and curr_str[-1] == "w" and all_chars == {"m", "e", "o", "w"}:
        return_str += "YES\n"
    else:
        return_str += "NO\n"

return_str = return_str.strip()

print(return_str)

# Test cases

# 7
# 4
# eooow
# 14
# moooooow
# 3
# meeeeeewwww
# 7
# meeeeeeoooo
# 4
# wwwwwww
# 6
# mmmmm
# 5
# eeeeee


# 7
# 4
# meOw
# 14
# mMmeoOoWWWwwwW
# 3
# mew
# 7
# MmeEeUw
# 4
# MEOW
# 6
# MmyaVW
# 5
# meowA
