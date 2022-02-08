class Dictionary():
    def __init__(self):
        self.lookup = dict()

    def newentry(self, word, definition):
        self.lookup[word] = definition

    def look(self, key):
        try:
            return self.lookup[key]
        except KeyError:
            return f"Can't find entry for {key}"



d = Dictionary()

d.newentry("Apple", "A fruit")
print(d.look("Apple"), "A fruit")

d.newentry("Soccer", "A sport")
print(d.look("Soccer"), "A sport")
print(d.look("Hi"), "Can't find entry for Hi")
print(d.look("Ball"), "Can't find entry for Ball")

d.newentry("soccer", "a sport")
print(d.look("soccer"), "a sport")
