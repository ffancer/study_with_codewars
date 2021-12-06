# 7 kyu
# FIXME: Get Full Name


class Dinglemouse(object):
    def __init__(self, first_name, last_name):
        first_name = first_name
        last_name = last_name
    def get_full_name(self):
        return first_name + ' ' + last_name


print(Dinglemouse('Clint', 'Eastwood').get_full_name(), 'Clint Eastwood')
print(Dinglemouse('', 'Eastwood').get_full_name(), 'Eastwood')
print(Dinglemouse('Clint', '').get_full_name(), 'Clint')
print(Dinglemouse('', '').get_full_name(), '')