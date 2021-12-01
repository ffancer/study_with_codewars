def bumps(road):
    cnt = 0

    for i in road:
        if i == 'n':
            cnt += 1

    return "Woohoo!" if cnt < 15 else "Car Dead"


print(bumps("n"), "Woohoo!")
print(bumps("_nnnnnnn_n__n______nn__nn_nnn"), "Car Dead")
print(bumps("______n___n_"), "Woohoo!")
print(bumps("nnnnnnnnnnnnnnnnnnnnn"), "Car Dead")
