import sys

f = sys.stdin.read().splitlines()
# f = [list(map(int, item.split())) for item in f]
line = f[1]
line_len = len(line)
left_lprefix = [None] * line_len
right_lprefix = [None] * line_len

ldict = {"L": 1, "R": 0}


for i, char in enumerate(line):
    if i == 0:
        left_lprefix[i] = ldict[char]
    else:
        left_lprefix[i] = left_lprefix[i - 1] + ldict[char]

for i, char in enumerate(line[::-1]):
    if i == 0:
        right_lprefix[line_len - 1 - i] = ldict[char]
    else:
        right_lprefix[line_len - 1 - i] = right_lprefix[line_len - i] + ldict[char]

min_num = float("inf")
for i, (left, right) in enumerate(zip(left_lprefix, right_lprefix)):
    left -= ldict[line[i]]
    right -= ldict[line[i]]

    right_min = line_len - i - 1 - right
    min_num = min(min_num, (right_min + left))

print(min_num)
