class Hero(object):
    def __init__(self, name):
        self.name = name
        self.experience = 0
        self.health = 100
        self.position = '00'
        self.damage = 5


def basic_test_cases():
    myHero = Hero()
    print(myHero.name, 'Hero')
    print(myHero.experience, 0)
    print(myHero.health, 100)
    print(myHero.position, '00')
    print(myHero.damage, 5)


print(basic_test_cases())
