def itemgetter(item):
    item['name']


def get_names(data):
    return list(map(itemgetter, data))


data = [
    {'name': 'Joe', 'age': 20},
    {'name': 'Bill', 'age': 30},
    {'name': 'Kate', 'age': 23}
]

print("should work correctly")(
    lambda: print(get_names(data), ['Joe', 'Bill', 'Kate']))
