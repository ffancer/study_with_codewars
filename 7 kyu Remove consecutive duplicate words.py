def remove_consecutive_duplicates(s):
    s = s.split()
    lst = []

    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            lst.append(s[i])

    return ' '.join(lst)


print(remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'),
      'alpha beta gamma delta alpha beta gamma delta')
