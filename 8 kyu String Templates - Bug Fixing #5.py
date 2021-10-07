def build_string(*args):
    return "I like {1}!".format(",".join(args))


print(build_string('Cheese','Milk','Chocolate'), 'I like Cheese, Milk, Chocolate!', 'Return the correct String')
print(build_string('Cheese','Milk'), 'I like Cheese, Milk!', 'Return the correct String')
print(build_string('Chocolate'), 'I like Chocolate!', 'Return the correct String')