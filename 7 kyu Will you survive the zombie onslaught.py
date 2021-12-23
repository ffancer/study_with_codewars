# 7 kyu
# Will you survive the zombie onslaught?


def zombie_shootout(zombies, distance, ammo):
    shot_zomb = 0

    while True:
        ammo -= 1
        distance -= 0.5
        zombies -= 1
        shot_zomb += 1
        if zombies == 0 or distance == 0 or ammo == 0:
            break

    return zombies, distance, ammo, shot_zomb


print(zombie_shootout(3, 10, 10), "You shot all 3 zombies.")
print(zombie_shootout(100, 8, 200), "You shot 16 zombies before being eaten: overwhelmed.")
print(zombie_shootout(50, 10, 8), "You shot 8 zombies before being eaten: ran out of ammo.")
