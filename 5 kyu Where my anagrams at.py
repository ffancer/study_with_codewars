def anagrams(word, words):
    lst_sorted = []
    lst = []

    for i in words:
        lst_sorted.append(sorted(i))

    for i in lst_sorted:
        if i == sorted(word):
            lst.append(i)
    return lst_sorted
    # return lst

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
