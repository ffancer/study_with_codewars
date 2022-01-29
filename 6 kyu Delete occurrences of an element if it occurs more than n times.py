def delete_nth(order, max_e):
    lst = []
    dct = {}

    for i in order:
        if i not in dct:
            dct[i] = 0
        else:
            dct[i] += 1
        if dct[i] < max_e:
            lst.append(i)
    return lst

    # dct = {i: order.count(i) for i in order}
    # return dct


print(delete_nth([20, 37, 20, 21], 1), [20, 37, 21])
print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3), [1, 1, 3, 3, 7, 2, 2, 2])
