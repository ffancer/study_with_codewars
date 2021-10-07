# best practice 1
def build_string(*args):
    return "I like {}!".format(", ".join(args))


# best practice 2
def build_string(*args):
    return "I like {0}!".format(", ".join(args))



# best practice 3
def build_string(*args):
    return "I like %s!" % ", ".join(args)


print(build_string('Cheese','Milk','Chocolate'), 'I like Cheese, Milk, Chocolate!', 'Return the correct String')
print(build_string('Cheese','Milk'), 'I like Cheese, Milk!', 'Return the correct String')
print(build_string('Chocolate'), 'I like Chocolate!', 'Return the correct String')