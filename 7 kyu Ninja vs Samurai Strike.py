# 7 kyu
# Ninja vs Samurai: Strike
from random import randint


class Warrior:
    def __init__(self, name, health=100):
        self.health = health
        self.name = name

        def strike(enemy, swings):
            # health cannot go below zero
            enemy.health = max([-1, enemy.health - (swings * 10)])


name = ['Hattori Hanzo', 'Sasuke Sarutobi', 'Jubei Kibagami', 'Kotaro Fuma'][randint(0, 3)]
ninja = Warrior(name)
print(ninja.name, name, "Making the 'name' variable visible will help you complete this kata")
