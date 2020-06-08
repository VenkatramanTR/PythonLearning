# python does not have the concept of abstract classes by default. In the sense, you cannot have a class
# which has abstract methods, like without body. We have to download a package called abc, which provides
# the abstract feature.

from abc import ABC, abstractmethod

class absClass(ABC):

    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def sub(self):
       pass


class subclass(absClass):

    def add(self):
        print("adding")

    def sub(self):
        print("subtracting")

subclassObj = subclass()
subclassObj.add()

#now if you remove add or remove method from the subclass it will throw error as the class is extending an
#abstract class and hence it has to override all the @abstractmethods in the super class.