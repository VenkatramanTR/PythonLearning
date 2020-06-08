# In python we dont directly have the concept of method overloading as how we have in java. We cannot
# have two methods with the same name in python. However method overloading is done here in a different way

class A:
    def add(self,a,b):
        return a+b
    def addOverloaded(self,a=0,b=0,c=0):
        return a+b+c;

a = A()
print(a.add(4,5))

#now if i want to pass three numbers to the same add method and sometimes i want to pass two numbers
#and sometimes I want to pass 1 number. So how come we can use the same metho to perform three different
#functionality? See the addOverloaded method

print(a.addOverloaded(4))
print(a.addOverloaded(4,5))
print(a.addOverloaded(4,5,6))