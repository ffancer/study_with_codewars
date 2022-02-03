def scramble(s1, s2):
    cnt = 0

    for i in s2:
        if i in s1:
            cnt += 1

    return cnt == len(s2)

print(scramble('rkqodlw', 'world'), True)
print(scramble('cedewaraaossoqqyt', 'codewars'), True)
print(scramble('katas', 'steak'), False)
print(scramble('scriptjava', 'javascript'), True)
print(scramble('scriptingjava', 'javascript'), True)
