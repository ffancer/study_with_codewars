from math import log


def logs(x, a, b):
    return log(a*b) / log(x)


print(logs(10, 2, 3), 0.7781512503836435)
print(logs(5, 2, 3), 1.1132827525593785)
print(logs(1000, 2, 3), 0.25938375012788123)
