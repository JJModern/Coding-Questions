def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    bought, not_bought, sold = 0, 0, float("-inf")

    for i, price in enumerate(prices):
        temp_tuple = (bought, not_bought, sold)

        bought = temp_tuple[1] - price
        not_bought = max(temp_tuple[1], sold)
        if temp_tuple[0] != 0:
            if temp_tuple[1] == 0:
                sold = max(temp_tuple[0] + price, sold)
            else:
                sold = max(temp_tuple[1], temp_tuple[0]) + price

    return max(bought, not_bought, sold)


prices = [1, 2, 4]
maxProfit(prices)
