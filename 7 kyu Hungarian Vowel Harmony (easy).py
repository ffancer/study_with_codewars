# -*- coding: utf-8 -*-
def dative(word):
    if ['e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű'] in word[-3:]:
        return word + 'nek'
    if ['a', 'á', 'o', 'ó', 'u', 'ú'] in word[-3:]:
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
