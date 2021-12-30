def band_name_generator(name):
    return f'{name.title() + name[1::]}' if name[0] == name[-1] else f'The {name.title()}'


print(band_name_generator("knife"), "The Knife")
print(band_name_generator("tart"), "Tartart")
print(band_name_generator("sandles"), "Sandlesandles")
print(band_name_generator("bed"), "The Bed")
print(band_name_generator("qq"), "Qqq")
