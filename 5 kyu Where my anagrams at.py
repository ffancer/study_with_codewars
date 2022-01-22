def anagrams(word, words):
    # return list(word)
    lst = []
    for i in words:
        for j in i:
            if j not in list(word):
                continue
            else:
                lst.append(i)
    return lst

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
