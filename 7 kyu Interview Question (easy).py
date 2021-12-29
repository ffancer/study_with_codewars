from collections import Counter


def get_strings(city):
    city = [i for i in city.lower() if i.isalpha()]
    city = Counter(city)

    return city
print(get_strings("Chicago"), "c:**,h:*,i:*,a:*,g:*,o:*")
print(get_strings("Bangkok"), "b:*,a:*,n:*,g:*,k:**,o:*")
print(get_strings("Las Vegas"), "l:*,a:**,s:**,v:*,e:*,g:*")
