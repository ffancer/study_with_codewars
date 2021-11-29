def max_number(n):
    return int(''.join(sorted(str(n), reverse=True)))

print(max_number(213), 321)
print(max_number(7389), 9873)
print(max_number(63792), 97632)
print(max_number(566797), 977665)
print(max_number(1000000), 1000000)
