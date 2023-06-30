def max_gain(cards):
    cards.reverse()
    dp = [0] * (len(cards) + 1)
    bonus_sum = 0
    max_bonus = 0

    for card in cards:
        if card == 0:  # Hero card
            for i in range(1, max_bonus + 1):
                total_power = bonus_sum - dp[i]
                dp[i] = max(dp[i], total_power)
            bonus_sum = 0
            max_bonus = 0
        else:  # Bonus card
            bonus_sum += card
            max_bonus += 1

    return dp[max_bonus]


def main():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        cards = list(map(int, input().strip().split()))
        results.append(max_gain(cards))

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

# all stacks
# normal deck
# bonus deck

# 0 is hero card

# this is dp.
# input (deck of list, k)
# deck w/o 0
# k: # of things to look for

# base case:
# when length is same as # of k
# return sum of all

# else
# recurse on all and see which one gets best.
# you could cache it if needed.

# 5
# 5
# 3 3 3 0 0
# 6
# 0 3 3 0 0 3
# 7
# 1 2 3 0 4 5 0
# 7
# 1 2 5 0 4 3 0
# 5
# 3 1 0 0 4


# ---

# def max_gain(lst, k):
#     first_zero = lst.index(0)
#     lst = lst[first_zero:]
#     if k == 0:
#         return 0
#     if k == 1:
#         if not lst:
#             return 0
#         else:
#             return max(lst)

#     if len(lst) - k == k:
#         return sum(lst)

#     # take one
#     # and then recurse
#     max_val = 0
#     for i, element in enumerate(lst):
#         if element != 0:
#             # remove last 0
#                 #get to second last 0

#             # control for each try except
#             try:
#                 second_zero = lst.index(0, 1)
#                 if second_zero < i:
#                     max_val = max(max_val,
#                           element + max_gain([0] + lst[i + 1:], k - 1))
#                 else:
#                     max_val = max(max_val,
#                           element + max_gain(lst[i + 1:], k - 1))
#             except:
#                 # means last zero
#                 max_val = max(max_val, element)

#     return max_val
