def correct(s):
    return s.replace('0', 'O').replace('1', 'I').replace('5', 'S')


print(correct("L0ND0N"), "LONDON")
print(correct("DUBL1N"), "DUBLIN")
print(correct("51NGAP0RE"), "SINGAPORE")
print(correct("BUDAPE5T"), "BUDAPEST")
print(correct("PAR15"), "PARIS")