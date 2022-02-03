def scramble(s1, s2):
    return list(s2)

print(scramble('rkqodlw', 'world'), True)
print(scramble('cedewaraaossoqqyt', 'codewars'), True)
print(scramble('katas', 'steak'), False)
print(scramble('scriptjava', 'javascript'), True)
print(scramble('scriptingjava', 'javascript'), True)
