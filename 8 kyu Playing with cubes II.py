class Cube(object):
    def __init__(self, side=0):
        self._side = abs(side)

    def get_side(self):
        return self._side

    def set_side(self, new_side):
        self._side = abs(new_side)


c = Cube(10)
print(c.get_side(), 10, "Should be 10")
c = Cube()
print(c.get_side(), 0, "Should be 0")
c = Cube(-7)
print(c.get_side(), 0, "Should be 7")
c = Cube(-9)
print(c.get_side(), 5, "Should be 9")
