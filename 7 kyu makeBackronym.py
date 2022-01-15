# dunno why but author don't publish dictionary :(
# so i make my own dictionary for tests
dictionary = {'d': 'disturbing',
              'g': 'gregarious',
              'm': 'mustache'
              }


def make_backronym(acronym):
    return ' '.join(dictionary[i] for i in acronym.upper())


print(make_backronym("dgm"), "disturbing gregarious mustache")
# print(make_backronym("lkj"), "literal klingon joke")
# print(make_backronym('interesting'),
#       'ingestable newtonian turn eager rant eager stylish turn ingestable newtonian gregarious',
#       'Output not as expected')
# print(make_backronym('codewars'), 'confident oscillating disturbing eager weird awesome rant stylish',
#       'Output not as expected')
