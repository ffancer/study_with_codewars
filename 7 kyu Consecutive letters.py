def solve(st):
    return sorted(st)


print(solve("abc"), True)
print(solve("abd"), False)
print(solve("dabc"), True)
print(solve("abbc"), False)
