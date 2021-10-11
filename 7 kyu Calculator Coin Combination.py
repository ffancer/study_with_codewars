# 7 kyu
# Calculator: Coin Combination

# best practice 1
def coin_combo(cents):
    return [cents % 5, ((cents % 25) % 10) // 5, (cents % 25) // 10, cents // 25]


# best practice 2
def coin_combo(cents):
    d = cents // 25
    c = (cents % 25) // 10
    b = ((cents % 25) % 10) // 5
    a = (((cents % 25) % 10) % 5) // 1
    return [a, b, c, d]


# best practice 3
def coin_combo(cents):
    coins = [1, 5, 10, 25]
    for i in range(3, -1, -1):
        coins[i], cents = divmod(cents, coins[i])
    return coins


print(coin_combo(1), [1, 0, 0, 0])
print(coin_combo(6), [1, 1, 0, 0])
print(coin_combo(11), [1, 0, 1, 0])
