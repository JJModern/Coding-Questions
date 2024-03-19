
# have a count dict for each 
    # have total inventory. through keys added.
# for each box, 


# sort all.

# move through, and move them in. 

import sys

f = sys.stdin.read().splitlines()
k = int(f[0].split()[1])

mylist = [item.split() for item in f[1:]]

total = 0
for sublist in mylist:
    total += k - len(set(sublist))

print(total)