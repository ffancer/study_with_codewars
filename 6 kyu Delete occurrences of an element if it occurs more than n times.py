def delete_nth(order, max_e):
    lst = []
    dct = {i: order.count(i) for i in order}

    for i, j in dct.items():
        if j <= max_e:
            lst.append(i)

    return lst


print(delete_nth([20, 37, 20, 21], 1), [20, 37, 21])
print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3), [1, 1, 3, 3, 7, 2, 2, 2])
