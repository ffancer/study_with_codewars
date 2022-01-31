class Person
    def __init__(name,age)
        self.info="#{name}s age is #{age}"



names=["john","matt","alex","cam"]
ages=[16,25,57,39]
for i in range(4):
    name,age=names[i],ages[i]
person=Person(name,age)
Person.info, name+"s age is "+str(age)