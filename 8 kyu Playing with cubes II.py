class Cube(object):
    # This cube needs help
    # Define a constructor which takes one integer, or handles no args

    def get_side(self):
        """Return the side of the Cube"""
        return self._side

    def set_side(self, new_side):
        """Set the value of the Cube's side."""
        self._side = new_side


c = Cube(10)
print(c.get_side(), 10, "Should be 10")
c = Cube()
print(c.get_side(), 0, "Should be 0")