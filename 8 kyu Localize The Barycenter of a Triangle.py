def bar_triang(pointA, pointB, pointC):
    return [round((pointA[0] + pointB[0] + pointC[0]) / 3, 4), round((pointA[1] + pointB[1] + pointC[1]) / 3, 4)]


print(bar_triang([4, 6], [12, 4], [10, 10]), [8.6667, 6.6667])
print(bar_triang([4, 2], [12, 2], [6, 10]), [7.3333, 4.6667])
print(bar_triang([4, 8], [8, 2], [16, 6]), [9.3333, 5.3333])
