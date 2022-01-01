def count_letters_and_digits(s):
    cnt_letters = 0

    for i in s:
        if i.isalpha() or i.isdigit():
            cnt_letters += 1

    return cnt_letters


print(count_letters_and_digits('n!!ice!!123'), 7)
print(count_letters_and_digits('de?=?=tttes!!t'), 8)
print(count_letters_and_digits(''), 0)
print(count_letters_and_digits('!@#$%^&`~.'), 0)
print(count_letters_and_digits('u_n_d_e_r__S_C_O_R_E'), 10)
