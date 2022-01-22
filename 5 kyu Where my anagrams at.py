from collections import Counter


def anagrams(word, words):
    lst = []

    for i in words:
        if Counter(i) == Counter(word):
            lst.append(i)

    return lst


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
