class Block:
    def get_width(self):
        pass

    def get_length(self):
        pass

    def get_height(self):
        pass

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
