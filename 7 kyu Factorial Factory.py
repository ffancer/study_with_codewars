from math import factorial as fctrl


def factorial(n):
    return fctrl(n) if n >= 0 else None


print(factorial(0), 1, 'Your math may be incorrect')
print(factorial(1), 1, 'Your math may be incorrect')
print(factorial(2), 2, 'Your math may be incorrect')
print(factorial(5), 120, 'Your math may be incorrect')
print(factorial(-1), None, "Don't forget to check for negatives!")
