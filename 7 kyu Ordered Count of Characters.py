def ordered_count(inp):
    dct = {i: inp.count(i) for i in inp}
    lst = []

    # lst = dct.items()

    return lst

print(ordered_count('abracadabra'))
print(ordered_count('Code Wars'))
