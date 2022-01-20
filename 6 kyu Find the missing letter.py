def find_missing_letter(chars):
    first = ord(chars[0])
    last = ord(chars[-1])
    lst = [chr(i) for i in range(first, last + 1)]

    return ''.join(i for i in lst if i not in chars)


print(find_missing_letter(['a', 'b', 'c', 'd', 'f']), 'e')
print(find_missing_letter(['O', 'Q', 'R', 'S']), 'P')