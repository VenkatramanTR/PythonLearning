class Student:
    def __init__(self, name , rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def showStudent(self):
        print(self.name,self.rollno)
        self.lap.showLaptop()

    class Laptop:
        def __init__(self):
            self.name = "Dell"
            self.color = "Silver"

        def showLaptop(self):
            print(self.name, self.color)

s1 = Student("Venkatraman", 1)
s2 = Student("Balaji", 2)


s1.showStudent()
s2.showStudent()



