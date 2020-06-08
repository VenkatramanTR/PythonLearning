# class methods, instance methods and static methods

class Student:
    school = 'padashaala'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return (self.m1 + self.m2 + self.m3)/3
    @classmethod
    def getSchoolName(cls):
        return cls.school
    @staticmethod
    def generalInfo():
        print(" This is a general information getting printed from a static method")


s1 = Student(45,66,77)
s2 = Student(56,45,65)

print(s1.average())
print(s2.average())
print(Student.getSchoolName())

s1.generalInfo()
