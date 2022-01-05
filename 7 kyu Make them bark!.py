def bark(self):
    return "Woof!"

Dog.bark = bark


apollo = Dog('Apollo', 'Dobermann', 'male', '4')
zeus = Dog('Zeus', 'Dobermann', 'male', '4')

print(apollo.bark(), 'Woof!')
print(zeus.bark(), 'Woof!')
