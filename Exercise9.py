# Жадібний алгоритм
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= count * coin
    return result

# Динамічне програмування
def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    result = {}
    i = amount
    for coin in sorted(coins, reverse=True):
        count = i // coin
        if count > 0:
            result[coin] = count
            i -= count * coin

    return result

# Приклад використання обох функцій
amount = 113
greedy_result = find_coins_greedy(amount)
dynamic_result = find_min_coins(amount)

print("Greedy Algorithm Result:", greedy_result)
print("Dynamic Programming Result:", dynamic_result)