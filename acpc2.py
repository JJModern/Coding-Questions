import sys

f = sys.stdin.read().splitlines()
mystring = f[0]

return_list = []
my_prev = ""

for char in mystring:
    if char != my_prev:
        return_list.append(char)
        my_prev = char

print("".join(return_list))
