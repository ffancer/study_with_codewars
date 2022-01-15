def scale(strng, k, n):
    return '\n'.join(''.join(j * k for j in i) for i in strng.split('\n') for _ in range(n)) if strng else ''


a = "abcd\nefgh\nijkl\nmnop"
r = "aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp"
print(scale(a, 2, 3), r)
print(scale("", 5, 5), "")
print(scale("Kj\nSH", 1, 2), "Kj\nKj\nSH\nSH")
