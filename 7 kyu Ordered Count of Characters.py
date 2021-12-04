def ordered_count(inp):
    dct = {i: inp.count(i) for i in inp}
    lst = [(key, dct[key]) for key in dct]

    return lst

print(ordered_count('abracadabra'))
print(ordered_count('Code Wars'))
