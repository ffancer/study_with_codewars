# 7 kyu
# Simple Fun #63: Shape Area

def shape_area(n):
    return pow(n, 2) + pow(n - 1, 2)


print(shape_area(2), 5)
print(shape_area(3), 13)
print(shape_area(1), 1)
print(shape_area(5), 41)
