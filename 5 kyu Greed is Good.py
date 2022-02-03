def score(dice):
    three_dice = [1000, 200, 300, 400, 500, 600]
    one_dice = [100, 0, 0, 0, 50, 0]
    total = 0

    for i in range(1, 7):
        cnt = dice.count(i)
        total += (cnt // 3) * three_dice[i - 1] + (cnt % 3) * one_dice[i - 1]

    return total


print(score([2, 3, 4, 6, 2]), 0)
print(score([4, 4, 4, 3, 3]), 400)
print(score([2, 4, 4, 5, 4]), 450)
