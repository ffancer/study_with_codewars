# best practice 1
def reverse_fun(n):
    for i in range(len(n)):
        n = n[:i] + n[i:][::-1]
    return n


# best practice 2
def reverse_fun(n):
    l = len(n)
    return ''.join(b + a for a, b in zip(list(n[:l // 2]) + [''], n[l // 2:][::-1]))


# best practice 3
def reverse_fun(n):
    n = n[::-1]
    for i in range(1, len(n)):
        n = n[:i] + n[i:][::-1]
    return n


print(reverse_fun('012345'), '504132')
print(reverse_fun('jointhedarkside'), 'ejdoiisnktrhaed')
