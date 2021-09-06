def combat(health, damage):
    return health - damage if health - damage > 0 else 0


print(combat(100, 5), 95)
print(combat(83, 16), 67)
print(combat(20, 30), 0)