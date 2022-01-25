from itertools import permutations as perm


def permutations(string):
    return list(set(''.join(i) for i in perm(string)))


print(permutations('a'), ['a'])
print(permutations('ab'), ['ab', 'ba'])
print(permutations('aabb'), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
