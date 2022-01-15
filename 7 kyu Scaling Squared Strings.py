def scale(strng, k, v):
    pass


a = "abcd\nefgh\nijkl\nmnop"
r = "aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp"
print(scale(a, 2, 3), r)
print(scale("", 5, 5), "")
print(scale("Kj\nSH", 1, 2), "Kj\nKj\nSH\nSH")
