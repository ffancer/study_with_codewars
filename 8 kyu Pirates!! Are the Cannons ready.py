def cannons_ready(gunners):
    a = [i for i in list(gunners.values())]
    b = ['aye' for j in range(len(a))]
    return 'Fire!' if a == b else 'Shiver me timbers!'

a = {'Mike': 'aye', 'Joe': 'aye', 'Johnson': 'aye', 'Peter': 'aye'}
b = {'Mike': 'aye', 'Joe': 'nay', 'Johnson': 'aye', 'Peter': 'aye'}
print(cannons_ready(a), 'Fire!')
print(cannons_ready(b), 'Shiver me timbers!')