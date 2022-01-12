# 7 kyu
# Naughty or Nice?


def get_nice_names(people):
    lst = []

    for i in people:
        if i['was_nice']:
            lst.append(i['name'])

    return lst


def get_naughty_names(people):
    lst = []

    for i in people:
        if not i['was_nice']:
            lst.append(i['name'])

    return lst


naughty = [{'name': 'xDranik', 'was_nice': False}]
nice = [{'name': 'Santa', 'was_nice': True}, {'name': 'Warrior reading this kata', 'was_nice': True}]

print(get_nice_names(naughty), [])
print(get_nice_names(nice), ['Santa', 'Warrior reading this kata'])
print(get_naughty_names(naughty), ['xDranik'])
print(get_naughty_names(nice), [])
