def remove_vowels(strng):
    return ''.join(i for i in strng if i not in 'aeiou')


print(remove_vowels("drake"), "drk")
print(remove_vowels("aeiou"), "")
