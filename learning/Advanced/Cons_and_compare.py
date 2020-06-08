class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare(self, other):
        if(self.age == other.age):
            print("they are the same")
        else:
            print("they are different")

person1 = Person("Venkat", 37)
person2 = Person("Balaji", 35)

person1.compare(person2)

