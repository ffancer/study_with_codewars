s = 'CodEWaRs'
lst = []

for i in s:
    if i.istitle():
        lst.append(s.find(i))

print(lst)