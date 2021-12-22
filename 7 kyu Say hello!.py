def greet(name):
    return None if name == '' or name is None else f'hello {name}!'


print(greet("Niks"), "hello Niks!", "didn't work for 'Niks'")
print(greet("Nick"), "hello Nick!", "didn't work for 'Nick'")
print(greet(""), None, "didn't work for empty string")
print(greet(None), None, "didn't work for None")
