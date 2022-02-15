def getSlope(p1, p2):
    (x, y), (x2, y2) = p1, p2
    try:
        return (y - y2) / (x - x2)
    except ZeroDivisionError:
        pass


# ("Should calculate the existing non-zero between 2 points")
print(getSlope([1, 1], [2, 2]), 1, "Incorrect Slope")
print(getSlope([11, 1], [1, 11]), -1, "Incorrect Slope")
# ("Should return None if the line passing through the points is vertical")
print(getSlope([1, 1], [1, 2]), None, "Incorrect Slope")
# ("Should return None if the same point is given twice")
print(getSlope([1, 1], [1, 1]), None, "Incorrect Slope")
