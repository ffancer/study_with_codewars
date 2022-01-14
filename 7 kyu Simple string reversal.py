def solve(s):
    if ' ' not in s:
        return s[::-1]

    space = s.index(' ')
    a = s.replace(' ', '')[::-1]

    return a[:space] + ' ' + a[space:]


print(solve("codewars"), "srawedoc")
print(solve("your code"), "edoc ruoy")
print(solve("your code rocks"), "skco redo cruoy")
print(solve("i love codewars"), "s rawe docevoli")
