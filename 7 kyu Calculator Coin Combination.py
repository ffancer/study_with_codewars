# 7 kyu
# Calculator: Coin Combination

def coin_combo(cents):
    lst = []

    for i in (25, 10, 5, 1):
        lst.append(cents // i)
        cents = cents % i

    return lst[::-1]


print(coin_combo(1), [1, 0, 0, 0])
print(coin_combo(6), [1, 1, 0, 0])
print(coin_combo(11), [1, 0, 1, 0])
