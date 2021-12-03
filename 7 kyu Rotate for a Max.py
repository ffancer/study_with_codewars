def max_rot(n):
    s, lst, i = str(n), [], 0

    while i < len(str(n)):
        s = s[:i] + s[i + 1:] + s[i]
        lst.append(int(s))
        i += 1

    return max(lst)


print(max_rot(38458215), 85821534)
print(max_rot(195881031), 988103115)
print(max_rot(896219342), 962193428)
print(max_rot(69418307), 94183076)
