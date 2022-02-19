class Cube(object):
    def __init__(self, side=0):
        self._side = side

    def get_side(self):
        return self._side

    def set_side(self, new_side):
        self._side = new_side


c = Cube(10)
print(c.get_side(), 10, "Should be 10")
c = Cube()
print(c.get_side(), 0, "Should be 0")
print(c.get_side(), -7, "Should be 7")
print(c.get_side(), -9, "Should be 9")