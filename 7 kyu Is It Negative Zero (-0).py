def is_negative_zero(n):
    return n


print(is_negative_zero(-0.0), True)
print(is_negative_zero(-(float("inf"))), False)
print(is_negative_zero(-5.0), False)
print(is_negative_zero(-4.0), False)
print(is_negative_zero(-3.0), False)
print(is_negative_zero(-2.0), False)
print(is_negative_zero(-1.0), False)
print(is_negative_zero(0.0), False)
print(is_negative_zero(1.0), False)
print(is_negative_zero(2.0), False)
print(is_negative_zero(3.0), False)
print(is_negative_zero(4.0), False)
print(is_negative_zero(5.0), False)
print(is_negative_zero(float("inf")), False)
