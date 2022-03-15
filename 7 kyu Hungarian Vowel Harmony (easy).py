def dative(word):
    if word == 'úr':
        return 'úrnak'
    if word[-1] in 'eéiíöőüű' or word[-2] in 'eéiíöőüű' or word[-3] in 'eéiíöőüű':
        return word + 'nek'
    if word[-1] in 'aáoóuú' or word[-2] in 'aáoóuú' or word[-3] in 'aáoóuú' or word[-4] in 'aáoóuú':
        return word + 'nak'


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
