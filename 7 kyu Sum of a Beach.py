def sum_of_a_beach(beach):  # "Sand", "Water", "Fish", and "Sun"
    beach = beach.lower()
    sand = beach.count('sand')

    return sand


print(sum_of_a_beach("SanD"), 1)
print(sum_of_a_beach("sunshine"), 1)
print(sum_of_a_beach("sunsunsunsun"), 4)
print(sum_of_a_beach("123FISH321"), 1)