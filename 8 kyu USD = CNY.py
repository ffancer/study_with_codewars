# 8 kyu USD => CNY
def usdcny(usd):
    return round(6.75 * usd, 2)


print(usdcny(15), "101.25 Chinese Yuan")
print(usdcny(465), "3138.75 Chinese Yuan")