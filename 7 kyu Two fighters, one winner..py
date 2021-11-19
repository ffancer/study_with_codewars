class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)

    __repr__ = __str__


def declare_winner(fighter1, fighter2, first_attacker):
    while fighter1.health > 0 and fighter2.health > 0:
        if first_attacker == fighter1:
            fighter2.health -= fighter1.damage_per_attack
            first_attacker = fighter2.name
        else:
            fighter1.health -= fighter2.damage_per_attack
            first_attacker = fighter1.name

    if fighter1.health <= 0:
        return fighter2.name
    return fighter1.name



print(declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew"), "Lew")
print(declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Harry"), "Harry")
print(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry"), "Harald")
print(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harald"), "Harald")
print(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry"), "Harald")
print(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Harald"), "Harald")
