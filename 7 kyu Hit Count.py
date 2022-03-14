def counter_effect(hit_count):
    # lst = []
    #
    # for i in hit_count:
    #     lst2 = []
    #     for j in range(0, int(i)+1):
    #         lst2.append(j)
    #
    # return lst2
    hit_count = [int(i) for i in hit_count]
    lst = []
    for i in hit_count:
        lst.append([j for j in range(0, i + 1)])
    return lst


print(counter_effect("1250"), [[0, 1], [0, 1, 2], [0, 1, 2, 3, 4, 5], [0]])
print(counter_effect("0050"), [[0], [0], [0, 1, 2, 3, 4, 5], [0]])
print(counter_effect('0000'), [[0], [0], [0], [0]])