class Block:
    def __init__(self, lst):
        self.width = lst[0]
        self.length = lst[1]
        self.height = lst[2]

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_height(self):
        return self.height

    def get_volume(self):
        return self.width * self.length * self.height

    def get_surface_area(self):
        pass


block1 = Block([2, 2, 2])
print(block1.get_width(), 2)
print(block1.get_length(), 2)
print(block1.get_height(), 2)
print(block1.get_volume(), 8)
print(block1.get_surface_area(), 24)
