def God():
    man = Man()
    woman = Woman()
    return [man, woman]


class Human:
    def __init__(self):
        pass


class Man(Human):
    def __init__(self):
        pass


class Woman(Human):
    def __init__(self):
        pass


paradise = God()
print(isinstance(paradise[0], Man), True, "First object are a man")
