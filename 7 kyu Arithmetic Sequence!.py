def nthterm(*args):
    return args[0] + args[1] * args[2]


print(nthterm(1, 2, 3), 7)
print(nthterm(2, 2, 2), 6)
print(nthterm(-50, 10, 20), 150)
