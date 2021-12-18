def remove_vowels(strng):
    return [i for i in strng if i in 'aeiou']


print(remove_vowels("drake"), "drk")
print(remove_vowels("aeiou"), "")
