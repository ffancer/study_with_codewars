def count_arara(n):
    # lst = ['anane', 'adak', 'adak anane', 'adak adak', 'adak adak anane', 'adak adak adak', 'adak adak adak anane', 'adak adak adak adak']
    #
    # return lst[n-1]
    anane = 'anane'  # it's 1
    adak = 'adak'  # it's 2


print(count_arara(1), "anane")
print(count_arara(2), "adak")
print(count_arara(3), "adak anane")
print(count_arara(9), "adak adak adak adak anane")
