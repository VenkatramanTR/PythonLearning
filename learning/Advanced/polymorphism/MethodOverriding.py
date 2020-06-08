class A:
    def info(self):
        print("parent class info")

class B(A):
    def info(self):
        print("child class info")

a = A()
a.info()
b = B()
b.info() # if the info method in class B is removed it calls the parent class info method, but if the child
         # overrides a method with the same signature as that of the parent class then that method is called
         # this concept is called method overriding.
