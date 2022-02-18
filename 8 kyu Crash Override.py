def alias_gen(f_name, l_name):
    try:
        return FIRST_NAME[f_name[0].upper()] + ' ' + SURNAME[l_name[0].upper()]
    except:
        return 'Your name must start with a letter from A - Z.'


basic_tests = (
    (('Mike', 'Millington'), 'Malware Mike'),
    (('Fahima', 'Tash'), 'Function T-Rex'),
    (('Daisy', 'Petrovic'), 'Data Payload'),
    (('Barny', 'White'), 'Beta Worm'),
    (('Hank', 'Kutz'), 'Half-life Killer'),
    (('123abc', 'Pinkman'), 'Your name must start with a letter from A - Z.'),
    (('walter', 'white'), 'WiFi Worm')
)

for names, result in basic_tests:
    print('{} {}'.format(*names))
    print(alias_gen(*names), result)
