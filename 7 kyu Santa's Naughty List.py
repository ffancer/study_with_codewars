def find_children(santas_list, children):
    lst = []

    for i in santas_list:
        if i in children:
            lst.append(i)

    return sorted(lst)


print(find_children(["Jason", "Jackson", "Jordan", "Johnny"], ["Jason", "Jordan", "Jennifer"]),
      ["Jason", "Jordan"], 'Does not pass basic test')
print(find_children(["Jason", "Jackson", "Johnson", "JJ"], ["Jason", "James", "JJ"]), ["JJ", "Jason"],
      'Does not pass sorting test')
print(find_children(["jASon", "JAsoN", "JaSON", "jasON"], ["JasoN", "jASOn", "JAsoN", "jASon", "JASON"]),
      ["JAsoN", "jASon"], 'Does not pass capitalization test')
