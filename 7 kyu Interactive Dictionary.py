class Dictionary():
    def __init__(self):
        pass

    def newentry(self, word, definition):
        pass

    def look(self, key):
        pass


d = Dictionary()

d.newentry("Apple", "A fruit")
print(d.look("Apple"), "A fruit")

d.newentry("Soccer", "A sport")
print(d.look("Soccer"), "A sport")
print(d.look("Hi"), "Can't find entry for Hi")
print(d.look("Ball"), "Can't find entry for Ball")

d.newentry("soccer", "a sport")
print(d.look("soccer"), "a sport")
