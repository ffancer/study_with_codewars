# 8 kyu
# Thinkful - Dictionary drills: Order filler

def fillable(stock, merch, n):
  return stock.get(merch, 0) >= n


stock = {
    'football': 4,
    'boardgame': 10,
    'leggos': 1,
    'doll': 5}

print(fillable(stock, 'football', 3), True)
print(fillable(stock, 'leggos', 2), False)
print(fillable(stock, 'action figure', 1), False)
