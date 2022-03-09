def make_password(phrase):
    phrase = phrase.split()
    s = ''

    for i in phrase:
        s += i[0]

    return s

print(make_password("Give me liberty or give me death"), "Gml0gmd",
      "Wrong output for 'Give me liberty or give me death'")
print(make_password("Keep Calm and Carry On"), "KCaC0", "Wrong output for 'Keep Calm and Carry On'")
