def solve(st):
    s = ''.join(sorted(st))

    for i in range(1, len(st)):
        if ord(s[i]) - ord(s[i - 1]) != 1:
            return False
    else:
        return True


print(solve("abc"), True)
print(solve("abd"), False)
print(solve("dabc"), True)
print(solve("abbc"), False)
# 3