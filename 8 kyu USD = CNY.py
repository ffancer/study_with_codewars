# 8 kyu USD => CNY
def usdcny(usd):
    return str("%.2f" % (6.75 * usd)) + ' Chinese Yuan'


print(usdcny(15), "101.25 Chinese Yuan")
print(usdcny(465), "3138.75 Chinese Yuan")
