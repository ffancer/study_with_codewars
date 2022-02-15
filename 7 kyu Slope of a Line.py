def getSlope(p1, p2):
    ''' Return the slope of the line through p1 and p2
    '''
    return None


# ("Should calculate the existing non-zero between 2 points")
print(getSlope([1, 1], [2, 2]), 1, "Incorrect Slope")
print(getSlope([11, 1], [1, 11]), -1, "Incorrect Slope")
# ("Should return None if the line passing through the points is vertical")
print(getSlope([1, 1], [1, 2]), None, "Incorrect Slope")
# ("Should return None if the same point is given twice")
print(getSlope([1, 1], [1, 1]), None, "Incorrect Slope")
