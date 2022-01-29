# 5 kyu
# Can you get the loop ?


def loop_size(n):
    lst = []

    while not n in lst:
        lst.append(n)
        n = n.next

    return len(lst) - lst.index(n)



