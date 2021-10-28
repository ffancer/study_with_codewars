def initialize_names(name):
    if len(name.split()[1:-1]) >= 1:
        return name.split()[0] + ' ' + '. '.join([i[0] for i in name.split()[1:-1]]) + '. ' + name.split()[-1]
    return name


print(initialize_names('Jack Ryan'), 'Jack Ryan')
print(initialize_names('Lois Mary Lane'), 'Lois M. Lane')
print(initialize_names('Dimitri'), 'Dimitri')
print(initialize_names('Alice Betty Catherine Davis'), 'Alice B. C. Davis')
print(initialize_names('Noel Marshall'))
