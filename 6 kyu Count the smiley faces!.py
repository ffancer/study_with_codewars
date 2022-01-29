def count_smileys(arr):
    cnt = 0
    for i in arr:
        print(i)


print(count_smileys([]), 0)
print(count_smileys([':D', ':~)', ';~D', ':)']), 4)
print(count_smileys([':)', ':(', ':D', ':O', ':;']), 2)
print(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)
