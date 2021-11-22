def words_to_marks(s):
    total = 0

    for i in s:
        total += ord(i) - 96

    return total


print(words_to_marks('attitude'), 100)
print(words_to_marks('friends'), 75)
print(words_to_marks('family'), 66)
print(words_to_marks('selfness'), 99)
print(words_to_marks('knowledge'), 96)
