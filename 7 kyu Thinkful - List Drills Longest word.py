def longest(words):
    max_len = 0

    for i in words:
        if len(i) > max_len:
            max_len = len(i)

    return max_len


print(longest(['simple', 'is', 'better', 'than', 'complex']), 7)
print(longest(['explicit', 'is', 'better', 'than', 'implicit']), 8)
print(longest(['beautiful', 'is', 'better', 'than', 'ugly']), 9)
