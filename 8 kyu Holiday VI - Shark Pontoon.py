def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    return "Alive!" if pontoon_distance/you_speed < shark_distance/shark_speed else "Shark Bait!"


print(shark(12, 50, 4, 8, True), "Alive!")
print(shark(7, 55, 4, 16, True), "Alive!")
print(shark(24, 0, 4, 8, True), "Shark Bait!")