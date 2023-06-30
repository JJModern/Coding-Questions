def line_segment_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    x_num = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
    y_num = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == 0:
        if (x1 - x2) * (y3 - y1) - (y1 - y2) * (x3 - x1) != 0:
            return "none"
        else:
            x_start = max(x1, x2, x3, x4)
            x_end = min(x1, x2, x3, x4)
            y_start = max(y1, y2, y3, y4)
            y_end = min(y1, y2, y3, y4)
            if x_start == x_end:
                return x_start, min(y_start, y_end), x_end, max(y_start, y_end)
            else:
                return min(x_start, x_end), y_start, max(x_start, x_end), y_end
    elif denom < 0:
        if x_num < 0 or x_num > denom:
            return "none"
        if y_num < 0 or y_num > denom:
            return "none"
        x_num = round(x_num / denom, 2)
        y_num = round(y_num / denom, 2)
        return (x_num, y_num)
    else:
        if x_num > 0 or x_num < denom:
            return "none"
        if y_num > 0 or y_num < denom:
            return "none"
        x_num = round(x_num / denom, 2)
        y_num = round(y_num / denom, 2)
        return (x_num, y_num)


import sys

f = sys.stdin.read().splitlines()
f = [list(map(int, item.split())) for item in f]

for i in range(1, f[0][0] + 1):
    (x1, y1), (x2, y2) = sorted(
        [(f[i][0], f[i][1]), (f[i][2], f[i][3])], key=lambda x: (x[0], x[1])
    )
    (x3, y3), (x4, y4) = sorted(
        [(f[i][4], f[i][5]), (f[i][6], f[i][7])], key=lambda x: (x[0], x[1])
    )
    result = line_segment_intersection(x1, y1, x2, y2, x3, y3, x4, y4)

    print(result)
