# 7 kyu
# Naughty or Nice?


def get_nice_names(people):
    return [i['name'] for i in people if i['was_nice']]


def get_naughty_names(people):
    return [i['name'] for i in people if not i['was_nice']]


naughty = [{'name': 'xDranik', 'was_nice': False}]
nice = [{'name': 'Santa', 'was_nice': True}, {'name': 'Warrior reading this kata', 'was_nice': True}]

print(get_nice_names(naughty), [])
print(get_nice_names(nice), ['Santa', 'Warrior reading this kata'])
print(get_naughty_names(naughty), ['xDranik'])
print(get_naughty_names(nice), [])
