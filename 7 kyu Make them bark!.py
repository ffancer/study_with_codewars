class Dog:
    def __init__(self, name, breed, sex, age):
        self.name = name
        self.breed = breed
        self.sex = sex
        self.age = age





apollo = Dog('Apollo', 'Dobermann', 'male', '4')
zeus = Dog('Zeus', 'Dobermann', 'male', '4')

test.assert_equals(apollo.bark(), 'Woof!')
test.assert_equals(zeus.bark(), 'Woof!')