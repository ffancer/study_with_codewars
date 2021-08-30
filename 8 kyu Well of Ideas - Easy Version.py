def well(x):
    return 'Publish!' if str(x).count('good') <= 2 else ('I smell a series!' if str(x).count('good') > 2 else 'Fail!')


print(well(['bad', 'bad', 'bad']), 'Fail!')
print(well(['good', 'bad', 'bad', 'bad', 'bad']), 'Publish!')
print(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']), 'I smell a series!')