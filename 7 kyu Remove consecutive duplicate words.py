def remove_consecutive_duplicates(s):
    lst = []

    for i in s.split():
        if i not in lst:
            lst.append(i)

    return lst


print(remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'),
      'alpha beta gamma delta alpha beta gamma delta')
