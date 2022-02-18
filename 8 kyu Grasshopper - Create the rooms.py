rooms = {'first': {
    'name': 'Bob',
    'description': 'bla-bla',
    'completed': 'yes'
}, 'second': {
    'name': 'Edgar',
    'description': 'bla-bla',
    'completed': 'no'
}, 'third': {
    'name': 'Ann',
    'description': 'bla-bla',
    'completed': "I don't know"
}}


def example_tests():
    def example_test_case():
        print(len(rooms) >= 3, 'Should have at least three rooms')

    def example_test_case():
        for name in rooms.values():
            print(isinstance(name, dict), f'{name} should be a dictionary')

    def example_test_case():
        for name in rooms.values():
            print(len(name) >= 3, f'Not enough properties for room: {name}')


print(example_tests())
