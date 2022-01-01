# 7 kyu
# Even or Odd - Which is Greater?


def even_or_odd(s):
    total_even, total_odd = 0, 0

    for i in s:
        if int(i) % 2 == 0:
            total_even += int(i)
        else:
            total_odd += int(i)

    if total_even == total_odd:
        return 'Even and Odd are the same'
    return 'Even is greater than Odd' if total_even > total_odd else 'Odd is greater than Even'


print(even_or_odd('12'), 'Even is greater than Odd')
print(even_or_odd('123'), 'Odd is greater than Even')
print(even_or_odd('112'), 'Even and Odd are the same')
