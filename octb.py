import sys

f = sys.stdin.read().splitlines()
f = [list(map(int, item.split())) for item in f]

n = f[0][0]

miny = float("inf")

for x1, y1, x2, y2 in f[1:]:
    # see if zero is in the middle of x1 and x2
    if min(x1, x2) <= 0 and max(x1, x2) >= 0 and max(y1, y2) >= 0:
        # horizontal and vertical
        if x1 == x2 and x1 == 0:
            miny = min(y1, y2, miny)
        elif y1 == y2:
            # see if zero is in the middle of x1 and x2
                miny = min(y1, miny)
        else:
            slope = 1.0 * (y2 - y1) / (x2 - x1)
            intercept = y1 - (slope * x1)
            if intercept > 0:
                 miny = min(intercept, miny)
if miny == float("inf"):
    print("-1.0")
else:
    print(miny)


