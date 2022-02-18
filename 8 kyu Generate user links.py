import urllib.parse


def generate_link(user):
    # user = user.split()
    # return f"http://www.codewars.com/users/{'%'.join(user)}"
    return urllib.parse.quote(user)


print(generate_link('matt c') ,'http://www.codewars.com/users/matt%20c')
print(generate_link('g964'), 'http://www.codewars.com/users/g964')
print(generate_link('GiacomoSorbi'), 'http://www.codewars.com/users/GiacomoSorbi')
print(generate_link('ZozoFouchtra'), 'http://www.codewars.com/users/ZozoFouchtra')
print(generate_link('colbydauph'),'http://www.codewars.com/users/colbydauph')
