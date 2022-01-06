def search_names(logins):
    return filter(lambda x: x[0][-1] == '_', logins)


a = [["foo", "foo@foo.com"], ["bar_", "bar@bar.com"]]
b = [["bar_", "bar@bar.com"]]
print(search_names(a), b)

a = [["foobar_", "foo@foo.com"], ["bar_", "bar@bar.com"]]
b = [["foobar_", "foo@foo.com"], ["bar_", "bar@bar.com"]]
print(search_names(a), b)

a = [["foo", "foo@foo.com"], ["bar", "bar@bar.com"]]
b = []
print(search_names(a), b)
