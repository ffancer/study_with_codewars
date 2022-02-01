def sum_of_a_beach(beach):
    beach = beach.lower()
    sand = beach.count('sand')
    water = beach.count('water')
    fish = beach.count('fish')
    sun = beach.count('sun')

    return sand + water + fish + sun


print(sum_of_a_beach("SanD"), 1)
print(sum_of_a_beach("sunshine"), 1)
print(sum_of_a_beach("sunsunsunsun"), 4)
print(sum_of_a_beach("123FISH321"), 1)