def solve(a, b):
    cnt_1, cnt_2, cnt_3 = 0,0,0

    for i in b:
        if i in a:
            cnt_1 += 1

    for j in b:
        if j in a:
            cnt_2 += 1

    for k in b:
        if k in a:
            cnt_3 += 1

    return [cnt_1, cnt_2, cnt_3]

print(solve(['abc', 'abc', 'xyz', 'abcd', 'cde'], ['abc', 'cde', 'uap']), [2, 1, 0])
print(solve(['abc', 'xyz', 'abc', 'xyz', 'cde'], ['abc', 'cde', 'xyz']), [2, 1, 2])
print(solve(['quick', 'brown', 'fox', 'is', 'quick'], ['quick', 'abc', 'fox']), [2, 0, 1])
