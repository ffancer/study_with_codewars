def cannons_ready(gunners):
    return 'Shiver me timbers!' if 'nay' in gunners.values() else 'Fire!'

a = {'Mike': 'aye', 'Joe': 'aye', 'Johnson': 'aye', 'Peter': 'aye'}
b = {'Mike': 'aye', 'Joe': 'nay', 'Johnson': 'aye', 'Peter': 'aye'}
print(cannons_ready(a), 'Fire!')
print(cannons_ready(b), 'Shiver me timbers!')