class parent1:
    def __init__(self):
        print("init of parent1")

    def feature1(self):
        print("feature 1 of parent1 is working")

    def feature2(self):
        print("feature 2 is working")


class child(parent1):
    def __init__(self):
        super().__init__()
        print("init of child")


class parent2:
    def __init__(self):
        print("init of parent2")

    def feature1(self):
        print("feature 1 of parent2 is working")

    def feature4(self):
        print("feature 4 is working")


class commonchild(parent1, parent2):
    def __init__(self):
        print("common child init")

    def feature5(self):
        print("feature 5 is working")

    def feature6(self):
        print("feature 6 is working")


child = child()


commonchildObj = commonchild()

commonchildObj.feature1()  # parent 1 is called because Method Order Execution is from left to right
# parent 1 is first super class and in the left so it is called.
