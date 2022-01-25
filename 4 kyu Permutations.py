from itertools import permutations as perm


def permutations(string):
    lst = [''.join(i) for i in perm(string)]
    lst = list(set(lst))
    return lst


print(permutations('a'), ['a'])
print(permutations('ab'), ['ab', 'ba'])
print(permutations('aabb'), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
