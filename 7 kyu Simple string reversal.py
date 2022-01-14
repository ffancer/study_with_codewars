def solve(s):
    if ' ' not in s:
        return s[::-1]

    space_lst = [i for i, j in enumerate(s) if j == ' ']

    # space = s.index(' ')
    # a = s.replace(' ', '')[::-1]
    # a[:space] + ' ' + a[space:]
    return space_lst


print(solve("codewars"), "srawedoc")
print(solve("your code"), "edoc ruoy")
print(solve("your code rocks"), "skco redo cruoy")
print(solve("i love codewars"), "s rawe docevoli")
