def longest(words):
    return max(len(i) for i in words)


print(longest(['simple', 'is', 'better', 'than', 'complex']), 7)
print(longest(['explicit', 'is', 'better', 'than', 'implicit']), 8)
print(longest(['beautiful', 'is', 'better', 'than', 'ugly']), 9)
