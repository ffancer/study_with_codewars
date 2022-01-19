def swap(string_):
    s = ''

    for i in string_:
        if i.islower():
            s += i.upper()
        else:
            s += i.lower()

    return s


print(swap('HelloWorld'), 'hELLOwORLD')
print(swap('CodeWars'), 'cODEwARS')
