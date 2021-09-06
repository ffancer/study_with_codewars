def reverse(st):
    st = list(st.split())[::-1]

    return ' '.join(st)



print(reverse('Hello World'), 'World Hello')
print(reverse('Hi There.'), 'There. Hi')