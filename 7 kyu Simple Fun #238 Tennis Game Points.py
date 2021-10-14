# 7 kyu
# Simple Fun #238: Tennis Game Points

# first
def tennis_game_points(score):
    arr = ["love", "15", "30", "40"]
    [a, b] = score.split("-")
    return arr.index(a) + (arr.index(a) if b == "all" else arr.index(b))

# second
points = {"15": 1, "30": 2, "40": 3}


def tennis_game_points(score):
    return sum(points.get(p, 0) for p in score.split("-")) * (2 if "all" in score else 1)


print(tennis_game_points("15-40"), 4)
print(tennis_game_points("30-all"), 4)
print(tennis_game_points("love-15"), 1)
print(tennis_game_points("love-30"), 2)
print(tennis_game_points("love-40"), 3)
print(tennis_game_points("15-love"), 1)
print(tennis_game_points("15-30"), 3)
