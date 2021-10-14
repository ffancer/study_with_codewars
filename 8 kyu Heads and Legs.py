def animals(heads, legs):
    if heads == legs == 0:
        return 0, 0

    if heads < 0 or legs < 0 or legs % 2 != 0:
        return "No solutions"

    cows = legs // 2 - heads
    chickens = heads - cows

    return (chickens, cows) if (chickens >= 0 and cows >= 0) else "No solutions"


print(animals(72, 200), (44, 28))
print(animals(116, 282), (91, 25))
print(animals(12, 24), (12, 0))
print(animals(6, 24), (0, 6))
print(animals(344, 872), (252, 92))
print(animals(158, 616), (8, 150))
print(animals(25, 555), "No solutions")
print(animals(12, 25), "No solutions")
print(animals(54, 956), "No solutions")
print(animals(5455, 54956), "No solutions")
print(animals(0, 0), (0, 0))
print(animals(-1, -1), "No solutions")
print(animals(500, 0), "No solutions")
print(animals(0, 500), "No solutions")
print(animals(-45, 5), "No solutions")
print(animals(5, -55), "No solutions")
