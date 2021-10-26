# best practice 1
def infected(s):
    lands = s.split('X')
    total = sum(map(len, lands))
    infected = sum(len(x) for x in lands if '1' in x)
    return infected * 100 / (total or 1)

# best practice 2
def infected(s):
    total = len(s)-s.count('X')
    infected = sum([len(i) for i in s.split('X') if '1' in i])
    return infected/total*100 if total > 0 else infected

# best practice 3
def infected(s):
    total_population = s.split('X')
    total = 0
    infected = 0
    for population in total_population:
        if "1" in population:
            infected += len(population)
        total += len(population)

    try:
        return (100 * infected) / total
    except ZeroDivisionError:
        return 0


print(infected("01000000X000X011X0X"))
print(infected("01X000X010X011XX"))
print(infected("XXXXX"))
print(infected("00000000X00X0000"))
print(infected("0000000010"))
print(infected("000001XXXX0010X1X00010"))
print(infected("X00X000000X10X0100"))
