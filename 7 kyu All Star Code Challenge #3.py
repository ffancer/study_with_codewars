def remove_vowels(strng):
    s = ''

    for i in strng:
        if i in ['a', 'e', 'i', 'o', 'u']:
            continue
        else:
            s += i

    return s


print(remove_vowels("drake"), "drk")
print(remove_vowels("aeiou"), "")
