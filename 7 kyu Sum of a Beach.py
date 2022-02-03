def sum_of_a_beach(beach):
    return sum(beach.lower().count(i) for i in ['sand', 'water', 'fish', 'sun'])


print(sum_of_a_beach("SanD"), 1)
print(sum_of_a_beach("sunshine"), 1)
print(sum_of_a_beach("sunsunsunsun"), 4)
print(sum_of_a_beach("123FISH321"), 1)