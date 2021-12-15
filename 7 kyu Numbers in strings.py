def solve(s):
    string_for_split = ''

    for i in s:
        if i.islower():
            string_for_split += ' '
        if i.isdigit():
            string_for_split += i

    lst = sorted(int(i) for i in string_for_split.split(' ') if i.isdigit())

    return lst[-1]


print(solve('gh12cdy695m1'), 695)
print(solve('2ti9iei7qhr5'), 9)
print(solve('vih61w8oohj5'), 61)
print(solve('f7g42g16hcu5'), 42)
print(solve('lu1j8qbbb85'), 85)
