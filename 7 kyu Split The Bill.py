def split_the_bill(x):
    total = sum(x.values())
    how_many_guests = len(x.values())

    return {i: round(j - (total / how_many_guests), 2) for i, j in x.items()}

print(split_the_bill({'A': 20, 'B': 15, 'C': 10}), {'A': 5, 'B': 0, 'C': -5})
print(split_the_bill({'A': 40, 'B': 25, 'X': 10}), {'A': 15, 'B': 0, 'X': -15})
