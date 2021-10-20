def draw_stairs(n):
    return '\n'.join([' ' * i + 'I' for i in range(n)])

print(draw_stairs(3))
print(draw_stairs(5))
print(draw_stairs(7))
