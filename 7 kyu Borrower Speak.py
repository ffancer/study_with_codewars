def borrow(s):
    return ''.join(i for i in s.lower() if i.isalpha())


print(borrow('WhAt! FiCK! DaMn CAke?'), 'whatfickdamncake')
print(borrow('THE big PeOpLE Here!!'), 'thebigpeoplehere')
print(borrow('i AM a TINY BoY!!'), 'iamatinyboy')