# -*- coding: utf-8 -*-
def dative(word):
    if [i for i in word[-3:]] in ['e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű'] :
        return word + 'nek'
    if [i for i in word[-3:]] in ['a', 'á', 'o', 'ó', 'u', 'ú']:
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
