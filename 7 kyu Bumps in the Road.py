# best practice
def bumps(road):
    return "Woohoo!" if road.count("n") <= 15 else "Car Dead"




print(bumps("n"), "Woohoo!")
print(bumps("_nnnnnnn_n__n______nn__nn_nnn"), "Car Dead")
print(bumps("______n___n_"), "Woohoo!")
print(bumps("nnnnnnnnnnnnnnnnnnnnn"), "Car Dead")
