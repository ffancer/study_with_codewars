def reverse(n):
    ans = 0

    while n > 0:
        digit = n % 10
        n = n // 10
        ans = ans * 10
        ans = ans + digit

    return ans

print(reverse(1234), 4321)
print(reverse(10987), 78901)
print(reverse(1020), 201)
