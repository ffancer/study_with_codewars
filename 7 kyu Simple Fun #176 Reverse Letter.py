def reverse_letter(string):
    s = ''
    for i in string:
        if i.isascii():
            s += i

    return s



print(reverse_letter("krishan"))

print(reverse_letter("ultr53o?n"))

print(reverse_letter("ab23c"))

print(reverse_letter("krish21an"))