def greedy_coin_change(amount, coins):  # type: ignore
    """Return a list of coins that add up to the amount using a greedy strategy. Assumes coins are sorted in descending order.
    """
    result = []
    for coin in coins:  # type: ignore
        while amount >= coin:
            amount -= coin  # type: ignore
            result.append(coin)  # type: ignore
    return result  # type: ignore


# coin denominations (sorted descending)

coins = [25, 10, 5, 1]

amount = 68  # For example, 68 cents

change = greedy_coin_change(amount, coins) # type: ignore

print("Coins used for 68 cents (greedy):", change)  # type: ignore
