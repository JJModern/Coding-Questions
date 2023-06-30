# def make_change(cents, drawer):

#     total_lst = []
#     if cents <= 0:
#         return [[]]

#     for denom, num in drawer.items():
#         if denom == cents:
#             total_lst += [[denom]]
#         if denom < cents and num > 0:
#             new_drawer = {k: v for k, v in drawer.items() if v > 0}
#             new_drawer[denom] -= 1
#             returned_lst_lst = make_change(cents - denom, new_drawer)
#             for item in returned_lst_lst:
#                 if item != []:
#                     total_lst += [[denom] + item]
#                 # here putting item in brackets messed everything up.
#                     #make sure you look at the format of each variable.
#     return total_lst


def make_change(change, drawer):
    ans = []
    if change < 0:
        return []
    if change == 0:
        return [ans]

    for denom, val in drawer.items():
        if val > 0:
            drawer[denom] -= 1
            part_ans = make_change(change - denom, drawer)
            for part in part_ans:
                part.append(denom)
                ans.append(part)
            drawer[denom] += 1

    return ans


print(make_change(7, {1: 3, 5: 2, 10: 1}))
print(make_change(7, {1: 8, 5: 2, 10: 1}))
print(make_change(7, {1: 3, 10: 1}))
print(make_change(0, {1: 8, 5: 2, 10: 1}))
print(make_change(25, {5: 7, 10: 1, 25: 1}))
print(make_change(72, {1: 4, 25: 1, 35: 3}))
