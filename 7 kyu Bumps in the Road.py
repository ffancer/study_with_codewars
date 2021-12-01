def bumps(road):
    return "Woohoo!" if sum(i == 'n' for i in road) <= 15 else "Car Dead"




print(bumps("n"), "Woohoo!")
print(bumps("_nnnnnnn_n__n______nn__nn_nnn"), "Car Dead")
print(bumps("______n___n_"), "Woohoo!")
print(bumps("nnnnnnnnnnnnnnnnnnnnn"), "Car Dead")
