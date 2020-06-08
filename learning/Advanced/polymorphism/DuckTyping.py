#if a bird quacks like duck, swims like duck and walks like duck then the bird is called duck, eventhough if
# that is not duck. Similarly any class which behaves in a certain way can be classified as same. Lets see one
#example of polymorphism where two classes having similar functionality can be interchanged.

class Pycharm:
    def execute(self):
        print("compiling")
        print("running")

class VisualStudioCode:
    def execute(self): #same method so can be an example of polymorphism
        print("spell check")
        print("compiling")
        print("running")

class Laptop:
    def code(self, classObj):
        print("going to code")
        classObj.execute()

laptop = Laptop()
laptop.code(Pycharm())
laptop.code(VisualStudioCode())

