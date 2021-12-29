class Block:
    def __init__(self, lst):
        self.width = lst[0]
        self.length = lst[1]
        self.height = lst[2]

    def get_width(self):
        return Block[0]

    def get_length(self):
        return Block[1]

    def get_height(self):
        return Block[2]

    def get_volume(self):
        pass

    def get_surface_area(self):
        pass


block1 = Block([2, 2, 2])
print(block1.get_width(), 2)
print(block1.get_length(), 2)
print(block1.get_height(), 2)
print(block1.get_volume(), 8)
print(block1.get_surface_area(), 24)
