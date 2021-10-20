# 7 kyu
# Simple Fun #189: Plant Doubling

def plant_doubling(n):
    return bin(n)[2:].count('1')

print(plant_doubling(5), 2)
print(plant_doubling(8), 1)
print(plant_doubling(536870911), 29)
print(plant_doubling(1), 1)
