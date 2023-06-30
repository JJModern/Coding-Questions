def minimumCosts(regular, express, expressCost):
    """
    :type regular: List[int]
    :type express: List[int]
    :type expressCost: int
    :rtype: List[int]
    """
    cost_list = []
    dpr, dpe = 0, expressCost

    for i, regular_cost in enumerate(regular):
        temp_dpe = min(dpr + expressCost, dpe) + express[i]
        temp_dpr = min(dpr, dpe) + regular_cost

        cost_list.append(min(temp_dpe, temp_dpr))

        dpe = temp_dpe
        dpr = temp_dpr

    return cost_list


regular = [1, 6, 9, 5]
express = [5, 2, 3, 10]
expressCost = 8

print(minimumCosts(regular, express, expressCost))
