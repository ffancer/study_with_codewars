def anagrams(word, words):
    lst_sorted = []
    lst = []

    for i in words:
        lst_sorted.append(sorted(i))


    # return lst_sorted
    return sorted(word)

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
