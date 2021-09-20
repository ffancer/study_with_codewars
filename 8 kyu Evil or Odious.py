def evil(n):
    return sum([int(i) for i in bin(n)[2:] if i == '1'])


print(evil(1),"It's Odious!")
print(evil(2),"It's Odious!")
print(evil(3),"It's Evil!")