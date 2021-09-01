def hello(name='World'):
    if len(name) < 1:
        return 'Hello, World!'
    return f'Hello, {name.capitalize()}!'
