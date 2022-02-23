def swap(st):
    vowels_lst = ['e', 'u', 'i', 'o', 'a']
    ans = ''

    for i in st:
        if i in vowels_lst:
            ans += i.upper()
        else:
            ans += i

    return ans


print(swap("HelloWorld!"), "HEllOWOrld!")
print(swap("Sunday"), "SUndAy")
