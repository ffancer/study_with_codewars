class Hero(object):
    def __init__(self, name):
        # Add default values here
        pass


def basic_test_cases():
    myHero = Hero()
    print(myHero.name, 'Hero')
    print(myHero.experience, 0)
    print(myHero.health, 100)
    print(myHero.position, '00')
    print(myHero.damage, 5)


print(basic_test_cases())
