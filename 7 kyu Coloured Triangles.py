def triangle(row):
    i, j = 0, 1
    while len(row) != 1:
        if row[i:j+1] in ['GG', 'BR', 'RB']:
            row = row.replace(row[i:j + 1], 'G')
        if row[i:j+1] in ['BB', 'RG', 'GR']:
            row = row.replace(row[i:j + 1], 'B')
        if row[i:j+1] in ['RR', 'BG', 'GB']:
            row = row.replace(row[i:j + 1], 'R')
    return row


# print(triangle('GB'), 'R')
# print(triangle('RRR'), 'R')
print(triangle('RGBG'), 'B')
print(triangle('RBRGBRB'), 'G')
# print(triangle('RBRGBRBGGRRRBGBBBGG'), 'G')
# print(triangle('B'), 'B')
