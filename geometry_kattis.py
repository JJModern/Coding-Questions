import sys

f = sys.stdin.read().splitlines()
f = [list(map(int, item.split())) for item in f]

# They are the same segment
#

# solve template

# print(f)

# def cross_product(x1, y1, x2, y2):
#     return x1 * y2 - y1 * x2

# 5
# -10 0 10 0 0 -10 0 10
# -10 0 10 0 -5 0 5 0
# 1 1 1 1 1 1 2 1
# 1 1 1 1 2 1 2 1
# 1871 5789 216 -517 189 -518 3851 1895

# parallel
# intersect
# on same line but not intersect

for i in range(1, f[0][0] + 1):
    (x1, y1), (x2, y2) = sorted(
        [(f[i][0], f[i][1]), (f[i][2], f[i][3])], key=lambda x: (x[0], x[1])
    )
    (x3, y3), (x4, y4) = sorted(
        [(f[i][4], f[i][5]), (f[i][6], f[i][7])], key=lambda x: (x[0], x[1])
    )

    v1 = f[i][2] - x1
    w1 = f[i][3] - f[i][1]

    v3 = f[i][4] - x1
    w3 = f[i][5] - f[i][1]

    v4 = f[i][6] - x1
    w4 = f[i][7] - f[i][1]

    cross_1 = v1 * w3 - w1 * v3
    cross_2 = v1 * w4 - w1 * v4

    x_print = None
    y_print = None
    if (x1, y1) == (x3, y3):
        x_print, y_print = (x1, y1)
    elif (x2, y2) == (x4, y4):
        x_print, y_print = (x2, y2)

    elif cross_1 * cross_2 < 0:
        # meet at one intersection
        if x1 == x2:
            x_print, y_print = (
                x1,
                (y4 - y3) / (x4 - x3) * x1 - ((y4 - y3) / (x4 - x3) * y3 - y3),
            )
        elif x3 == x4:
            x_print, y_print = (
                x3,
                (y2 - y1) / (x2 - x1) * x3 - ((y2 - y1) / (x2 - x1) * y1 - y1),
            )

        else:
            m = (y2 - y1) / (x2 - x1)
            n = (y4 - y3) / (x4 - x3)
            x = (y3 - n * x3 + m * x1 - y1) / (m - n)
            y = m * x - (m * x1 - y1)
            x_print, y_print = (x, y)

    elif cross_1 * cross_2 > 0:
        pass

    else:
        # calculate for below boolean
        first_lst = sorted([(x1, y1), (x2, y2)], key=lambda x: (x[0], x[1]))
        second_lst = sorted([(x3, y3), (x4, y4)], key=lambda x: (x[0], x[1]))

        left_max = sorted([first_lst[0], second_lst[0]], key=lambda x: (-x[0], -x[1]))
        right_min = sorted([first_lst[1], second_lst[1]], key=lambda x: (x[0], x[1]))

        x1 = left_max[0][0]
        x2 = right_min[0][0]

        y1 = left_max[0][1]
        y2 = right_min[0][1]

        if x1 > x2 or y1 > y2:
            pass
        else:
            print("{:.2f}  {:.2f}  {:.2f}  {:.2f}".format(x1, y1, x2, y2))
            continue

    if x_print is None:
        print("none")
    else:
        print(f"{x_print:.2f} {y_print:.2f}")
