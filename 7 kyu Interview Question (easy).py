def get_strings(city):
    s = ''

    for i in city:
        if i.isalpha():
            s += f'{i}:{"*" * city.count(i)}'

    return s
print(get_strings("Chicago"), "c:**,h:*,i:*,a:*,g:*,o:*")
print(get_strings("Bangkok"), "b:*,a:*,n:*,g:*,k:**,o:*")
print(get_strings("Las Vegas"), "l:*,a:**,s:**,v:*,e:*,g:*")
