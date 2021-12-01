def triangle(row):
    i, j = 0, 1
    while len(row) != 1:
        if 'GG' in row[i:j+1]:
            row = 'G' + row[j+1:]
        elif 'BG' or 'GB' in row[i:j+1]:
            row = 'R' + row[j+1:]
        elif 'RG' or 'GR' in row[i:j + 1]:
            row = 'B' + row[j + 1:]
        elif 'BR' or 'RB' in row[i:j + 1]:
            row = 'G' + row[j + 1:]
        i += 1
        j += 1
    return row
# print(triangle('GGBR'), 'R')

print(triangle('GB'), 'R')
print(triangle('RRR'), 'R')
print(triangle('RGBG'), 'B')
print(triangle('RBRGBRB'), 'G')
print(triangle('RBRGBRBGGRRRBGBBBGG'), 'G')
print(triangle('B'), 'B')
