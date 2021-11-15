def converter(mpg):
    return round(mpg * 1.609344/4.54609188, 2)

print(converter(12), 4.25)
print(converter(24), 8.50)
print(converter(36), 12.74)