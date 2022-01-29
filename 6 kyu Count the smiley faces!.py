def count_smileys(arr):
    lst = []

    for i in arr:
        if i[0] in [':', ';']:
            if i[1] in ['-', '~', ')', 'D']:
                if i[-1] in ['-', '~', ')', 'D']:
                    lst.append(i)

    return len(lst)


print(count_smileys([]), 0)
print(count_smileys([':D', ':~)', ';~D', ':)']), 4)
print(count_smileys([':)', ':(', ':D', ':O', ':;']), 2)
print(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)
print(count_smileys([';-]', ':-[', ';~*', ':~$', ';D']), 1)
