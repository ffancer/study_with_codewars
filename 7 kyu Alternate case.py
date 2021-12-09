def alternate_case(s):
    answer = ''

    for i in s:
        if i.islower():
            answer += i.capitalize()
        else:
            answer += i.lower()

    return answer


print(alternate_case("ABC"), "abc")
print(alternate_case(""), "")
print(alternate_case(" "), " ")
print(alternate_case("Hello World"), "hELLO wORLD")
print(alternate_case("cODEwARS"), "CodeWars")
print(alternate_case("i LIKE MAKING KATAS VERY MUCH"), "I like making katas very much")
