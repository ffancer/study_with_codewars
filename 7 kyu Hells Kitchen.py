def gordon(a):
    lst = []
    a = a.split()
    # vowels = ['a', 'e', 'i', 'o', 'u']

    for i in a:
        lst.append(i.upper().replace('A', '@').replace('E', '*').replace('I', '*').replace('O', '*').replace('U', '*') + '!!!!')
    return lst

print(gordon('What feck damn cake'), 'WH@T!!!! F*CK!!!! D@MN!!!! C@K*!!!!')
print(gordon('are you stu pid'), '@R*!!!! Y**!!!! ST*!!!! P*D!!!!')
print(gordon('i am a chef'), '*!!!! @M!!!! @!!!! CH*F!!!!')
print(gordon('dont you talk tome'), 'D*NT!!!! Y**!!!! T@LK!!!! T*M*!!!!')
print(gordon('how dare you feck'), 'H*W!!!! D@R*!!!! Y**!!!! F*CK!!!!')
