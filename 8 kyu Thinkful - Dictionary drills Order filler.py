# 8 kyu
# Thinkful - Dictionary drills: Order filler

def fillable(stock, merch, n):
    if merch in stock:
        if stock[merch] >= n:
            return True
        return False
    return False


stock = {
    'football': 4,
    'boardgame': 10,
    'leggos': 1,
    'doll': 5}

print(fillable(stock, 'football', 3), True)
print(fillable(stock, 'leggos', 2), False)
print(fillable(stock, 'action figure', 1), False)
