from collections import Counter
def anagrams(word, words):
    # return Counter(word)
    for i in words:
        print(Counter(i))

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
