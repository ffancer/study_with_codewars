def solve(a, b):
    return [a.count(i) for i in b]


print(solve(['abc', 'abc', 'xyz', 'abcd', 'cde'], ['abc', 'cde', 'uap']), [2, 1, 0])
print(solve(['abc', 'xyz', 'abc', 'xyz', 'cde'], ['abc', 'cde', 'xyz']), [2, 1, 2])
print(solve(['quick', 'brown', 'fox', 'is', 'quick'], ['quick', 'abc', 'fox']), [2, 0, 1])