# 8 kyu USD => CNY
def usdcny(usd):
    return f'{round(6.75 * usd, 2)} Chinese Yuan'


print(usdcny(15), "101.25 Chinese Yuan")
print(usdcny(465), "3138.75 Chinese Yuan")