def sort_my_string(S):
    even_lst, odd_lst = [], []

    for i, j in enumerate(S):
        if i % 2 == 0:
            even_lst.append(j)
        else:
            odd_lst.append(j)

    return ''.join(even_lst + [' '] + odd_lst)


print(sort_my_string("CodeWars"), "CdWr oeas")
print(sort_my_string("YCOLUE'VREER"), "YOU'RE CLEVER")
