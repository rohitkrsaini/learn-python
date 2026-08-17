class animal:
    def shound(self):
        print("some sound")

class dog:
    def shound(self):
        print("bark")

a = animal()
a.shound()
b = dog()
b.shound()

# informal polimophim

class animal:
    def shound(self):
        print("some sound")

class dog: 
    def shound(self):
        print("bark")

def render(obj):
    obj.shound()

render(dog())
render(animal())

