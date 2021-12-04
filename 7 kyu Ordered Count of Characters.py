def ordered_count(inp):
    return [(key, {i: inp.count(i) for i in inp}[key]) for key in {i: inp.count(i) for i in inp}]


print(ordered_count('abracadabra'))
print(ordered_count('Code Wars'))
