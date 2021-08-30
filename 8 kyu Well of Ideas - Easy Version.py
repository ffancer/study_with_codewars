def well(x):
    # first
    cnt = str(x).count('good')

    if cnt > 2:
        return 'I smell a series!'
    elif cnt == 1 or cnt == 2:
        return 'Publish!'
    else:
        return 'Fail!'

print(well(['bad', 'bad', 'bad']), 'Fail!')
print(well(['good', 'bad', 'bad', 'bad', 'bad']), 'Publish!')
print(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']), 'I smell a series!')