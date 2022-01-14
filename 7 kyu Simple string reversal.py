def solve(s):
    s_reverse_list = list(''.join(s[::-1].split()))

    for i, j in enumerate(s):
        if j == ' ':
            s_reverse_list.insert(i, ' ')

    return s_reverse_list

print(solve("codewars"), "srawedoc")
print(solve("your code"), "edoc ruoy")
print(solve("your code rocks"), "skco redo cruoy")
print(solve("i love codewars"), "s rawe docevoli")
