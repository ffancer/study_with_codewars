def solve(st, a, b):
    return st[:a] + st[a:b+1][::-1] + st[b+1:]



print(solve("codewars", 1, 5), "cawedors")
print(solve("codingIsFun", 2, 100), "conuFsIgnid")
print(solve("FunctionalProgramming", 2, 15), "FuargorPlanoitcnmming")
print(solve("abcefghijklmnopqrstuvwxyz", 0, 20), "vutsrqponmlkjihgfecbawxyz")
print(solve("abcefghijklmnopqrstuvwxyz", 5, 20), "abcefvutsrqponmlkjihgwxyz")
