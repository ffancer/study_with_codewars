def dative(word):
    for c in word[::-1]:
        if c in u'eéiíöőüű':
            return word+'nek'
        elif c in u'aáoóuú':
            return word+'nak'


print(dative(u"ablak"), u"ablaknak")
print(dative(u"tükör"), u"tükörnek")
print(dative(u"keret"), u"keretnek")
print(dative(u"otthon"), u"otthonnak")
print(dative(u"virág"), u"virágnak")
print(dative(u"tett"), u"tettnek")
print(dative(u"rokkant"), u"rokkantnak")
print(dative(u"rossz"), u"rossznak")
print(dative(u"gonosz"), u"gonosznak")
print(dative(u"rög"), u"rögnek")
print(dative(u"király"), u"királynak")
