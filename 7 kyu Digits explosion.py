def explode(s):
    ans = ''

    for i in s:
        ans += i * int(i)

    return ans


print(explode("312"), "333122")
print(explode("102269"), "12222666666999999999")
print(explode("0"), "")
print(explode("000"), "")
print(explode("123"), "122333")
