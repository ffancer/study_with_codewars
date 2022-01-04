from math import pi


def circle_area(r):
    if type(r) != int or r <= 0:
        return False
    return round(r ** 2 * pi, 2)


print(circle_area(2), 12.57, "Incorrect radius")
print(circle_area(-3), False, "Negative radii don't have circle areas")
print(circle_area('An Integer'), False, "Strings can't generate areas")
print(circle_area(0), False, "Radius of 0 can't generate an area")
