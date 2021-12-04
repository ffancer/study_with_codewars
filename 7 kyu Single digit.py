def single_digit(n):
    if len(str(n)) == 1:
        return n
    cnt = bin(n)[2::].count('1')
    return cnt if cnt <= 9 else bin(cnt)[2::].count('1')


print(single_digit(5), 5)
print(single_digit(5665), 5)
print(single_digit(123456789), 1)
