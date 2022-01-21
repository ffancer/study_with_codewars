def dig_pow(n, p):
    s = 0
    for i, j in enumerate(str(n)):
        s += pow(int(j), i + p)

    return s//n


print(dig_pow(89, 1), 1)
print(dig_pow(92, 1), -1)
print(dig_pow(46288, 3), 51)
