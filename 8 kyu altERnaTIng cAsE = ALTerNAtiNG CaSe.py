def to_alternating_case(string):
    s = ''

    for i in string:
        if i.islower():
            s += i.upper()
        elif i.isupper():
            s += i.lower()
        else:
            s += i

    return s






print(to_alternating_case("hello world"))
print(to_alternating_case("HELLO WORLD"))
print(to_alternating_case("hello WORLD"))
print(to_alternating_case("HeLLo WoRLD"))
print(to_alternating_case("12345"))
print(to_alternating_case("1a2b3c4d5e"))
print(to_alternating_case("String.prototype.toAlternatingCase"))
print(to_alternating_case(to_alternating_case("Hello World")))

