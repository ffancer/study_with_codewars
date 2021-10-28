# best practice 1:
def closest_multiple_10(i):
    return round(i, -1)


# best practice 2:
def closest_multiple_10(i):
    return round(i / 10) * 10


# best practice 3:
def closest_multiple_10(i):
    r = i % 10
    return i - r if r < 5 else i - r + 10


# best practice 4:
closest_multiple_10 = lambda x: round(x, -1)

print(closest_multiple_10(54), 50)
print(closest_multiple_10(55), 60)
