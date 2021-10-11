# 7 kyu
# Calculator: Coin Combination

def coin_combo(cents):
    coins = [0, 0, 0, 0]

    while cents >= 25:
        coins[3] += 1
        cents -= 25

    while cents >= 10:
        coins[2] += 1
        cents -= 10

    while cents >= 5:
        coins[1] += 1
        cents -= 5

    while cents >= 1:
        coins[0] += 1
        cents -= 1

    return coins


print(coin_combo(1), [1, 0, 0, 0])
print(coin_combo(6), [1, 1, 0, 0])
print(coin_combo(11), [1, 0, 1, 0])
