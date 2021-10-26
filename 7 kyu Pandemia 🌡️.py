def infected(s):
    answer = ''

    for i in s.split('X'):
        if '1' in i:
            for j in i:
                if j == '0':
                    answer += '1'
                else:
                    answer += j

    try:
        return 100 * answer.count('1') / len(s.replace('X', ''))
    except:
        return 0


print(infected("01000000X000X011X0X"))
print(infected("01X000X010X011XX"))
print(infected("XXXXX"))
print(infected("00000000X00X0000"))
print(infected("0000000010"))
print(infected("000001XXXX0010X1X00010"))
print(infected("X00X000000X10X0100"))
