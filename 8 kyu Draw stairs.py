def draw_stairs(n):
    s = ''

    for i in range(n):
        s += ' ' * i + 'I' + '\n'

    return s[:-1]

print(draw_stairs(3))
print(draw_stairs(5))
print(draw_stairs(7))
