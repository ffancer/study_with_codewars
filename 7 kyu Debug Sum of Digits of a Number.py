def get_sum_of_digits(num):
    sum = ''
    digits = str(num)
    for x in digits:
        sum += x
    return sum


print(get_sum_of_digits(123), 6)
