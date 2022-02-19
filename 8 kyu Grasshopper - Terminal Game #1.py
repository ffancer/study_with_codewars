class Hero(object):
    def __init__(self, name='Hero', experience=0, health=100, position='00', damage=5):
        self.name = name
        self.experience = experience
        self.health = health
        self.position = position
        self.damage = damage


def basic_test_cases():
    myHero = Hero()
    print(myHero.name, 'Hero')
    print(myHero.experience, 0)
    print(myHero.health, 100)
    print(myHero.position, '00')
    print(myHero.damage, 5)


print(basic_test_cases())
