def correct(s):
    # first
    # return s.replace('0', 'O').replace('1', 'I').replace('5', 'S')

    # second
    answer = ''

    for i in s:
        if i == '0':
            answer += 'O'
        elif i == '1':
            answer += 'I'
        elif i == '5':
            answer += 'S'
        else:
            answer += i

    return answer

print(correct("L0ND0N"), "LONDON")
print(correct("DUBL1N"), "DUBLIN")
print(correct("51NGAP0RE"), "SINGAPORE")
print(correct("BUDAPE5T"), "BUDAPEST")
print(correct("PAR15"), "PARIS")