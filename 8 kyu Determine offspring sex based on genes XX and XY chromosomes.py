def chromosome_check(sperm):
    return 'Congratulations! You\'re going to have a son.' if 'XY' in sperm else 'Congratulations! You\'re going to have a daughter.'


print(chromosome_check('XY'), 'Congratulations! You\'re going to have a son.')
print(chromosome_check('XX'), 'Congratulations! You\'re going to have a daughter.')
