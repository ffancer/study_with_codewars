def reverse(st):
    return ' '.join(list(st.split())[::-1])


print(reverse('Hello World'), 'World Hello')
print(reverse('Hi There.'), 'There. Hi')