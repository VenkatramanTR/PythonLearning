class parent1:
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")

class parent2:
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")

class commonchild(parent2,parent1):
    def feature5(self):
        print("feature 5 is working")
    def feature6(self):
        print("feature 6 is working")

class child(parent1):
    def feature6(self):
        print("feature 6 is working")

class grandchild(child):
    def feature7(self):
        print("feature 7 is working")

parent1 = parent1()
parent2 = parent2()
commonchild = commonchild()
child = child()
grandchild = grandchild()

print("parent 1 can have feature 1 and 2")
parent1.feature1()
parent1.feature2()

print("parent 2 can have feature 3 and 4")
parent2.feature3()
parent2.feature4()


print("commonchild can have feature 1, 2, 3, 4, 5 and 6 and this is called multiple inheritance")
commonchild.feature1()
commonchild.feature2()
commonchild.feature3()
commonchild.feature4()
commonchild.feature5()
commonchild.feature6()

print("child can have feature 1, 2 and 6")
child.feature1()
child.feature2()
child.feature6()

print("grandchild can have feature 1, 2, 6 and 7 and this is called multi level inheritance")
grandchild.feature1()
grandchild.feature2()
grandchild.feature6()
grandchild.feature7()
