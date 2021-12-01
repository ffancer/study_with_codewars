def triangle(row):
    i, j = 0, 1
    s = ''

    while j < len(row):
        if row[i:j+1] in ['GG', 'BR', 'RB']:
            s += 'G'
        if row[i:j+1] in ['BB', 'RG', 'GR']:
            s += 'B'
        if row[i:j+1] in ['RR', 'BG', 'GB']:
            s += 'R'
        i += 1
        j += 1
        row = s

    return row


print(triangle('GB'), 'R')
print(triangle('RRR'), 'R')
print(triangle('RGBG'), 'B')
print(triangle('RBRGBRB'), 'G')
print(triangle('RBRGBRBGGRRRBGBBBGG'), 'G')
print(triangle('B'), 'B')
