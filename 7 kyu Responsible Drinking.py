def hydrate(drink_string):
    total = 0

    for i in drink_string:
        if i.isdigit():
            total += int(i)

    return f'{total} glass of water'


print(hydrate("1 beer"), "1 glass of water")
print(hydrate("1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer"), "10 glasses of water")
