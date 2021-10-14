# 7 kyu
# Simple Fun #238: Tennis Game Points

def tennis_game_points(score):
    dct = {
        'love': 0,
        '15': 1,
        '30': 2,
        '40': 3,
        'all': 2
    }
    score = score.split('-')
    total = 0

    for i in score:
        # total += dct.get(i)
        total += dct[i]

    return total

print(tennis_game_points("15-40"), 4)
print(tennis_game_points("30-all"), 4)
print(tennis_game_points("love-15"), 1)
print(tennis_game_points("love-30"), 2)
print(tennis_game_points("love-40"), 3)
print(tennis_game_points("15-love"), 1)
print(tennis_game_points("15-30"), 3)