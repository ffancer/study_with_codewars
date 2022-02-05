def decode(s):
    alphabet = "!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,? "
    alph_len = len(alphabet)
    answer = ''

    for i, j in enumerate(s, 1):
        k = [alphabet[2 ** i * v % alph_len] for v in range(len(alphabet))]
        answer += alphabet[k.index(j)] if j in k else j

    return answer


print(decode('hello world'))
print(decode('("!@#$%^&*()_+-")'))
