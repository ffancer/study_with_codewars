def borrow(s):
    ans = ''

    for i in s.lower():
        if i.isalpha():
            ans += i

    return ans


print(borrow('WhAt! FiCK! DaMn CAke?'), 'whatfickdamncake')
print(borrow('THE big PeOpLE Here!!'), 'thebigpeoplehere')
print(borrow('i AM a TINY BoY!!'), 'iamatinyboy')