def sakura_fall(v):
    return 0 if v <= 0 else round(400 / v, 15)



print(sakura_fall(5), 80)
print(sakura_fall(10), 40)
print(sakura_fall(-1), 0)
