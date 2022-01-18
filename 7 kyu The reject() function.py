def reject(seq, predicate):
    return [i for i in seq if not predicate(i)]


print(reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0), [1, 3, 5])
print(reject(['a', 'b', 3, 'd'], lambda x: type(x) == int), ['a', 'b', 'd'])
print(reject(['a', 'b', 3, 'd'], lambda x: type(x) == str), [3])
