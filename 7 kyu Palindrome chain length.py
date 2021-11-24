def palindrome_chain_length(n):
    cnt = 0
    n = n + int(str(n)[::-1])
    while str(n) != str(n)[::-1]:
        cnt += 1
        n = int(n) + int(str(n)[::-1])
    return cnt + 1

print(palindrome_chain_length(1), 0)
print(palindrome_chain_length(88), 0)
print(palindrome_chain_length(87), 4)
print(palindrome_chain_length(89), 24)
print(palindrome_chain_length(10), 1)
