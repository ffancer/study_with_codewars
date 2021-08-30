from math import sqrt

lst = [4, 3, 9, 7, 2, 1]
lst_answer = []
for i in lst:
    print(sqrt(i))
    if str(sqrt(i))[2] == '0':
        lst_answer.append(int(sqrt(i)))
    else:
        lst_answer.append(i ** 2)
print(lst_answer)