# whenever we do operations like +,-,/,* behind the scenes some methods are called like __add__, __sub__ etc
# here we will see how we can use these operators in our custom class to perform some operations

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        s1 = self.m1 + other.m1
        s2 = self.m2 + other.m2
        s3 = Student(s1,s2)
        return s3

s1 = Student(65,60)
s2 = Student(55,65)

s3 = s1+s2  # here the + symbol is calling the __add__ method, similarly you can do for +,-,*,/,<,>,>= etc
print(s3.m1, s3.m2)


