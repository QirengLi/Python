def maximumWealth(accounts):
    max_wealth = 0

    for wealth in accounts:
        max_wealth = max(max_wealth, sum(wealth))
    return max_wealth

