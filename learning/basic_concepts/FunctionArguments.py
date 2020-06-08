def immutableObjects(x):
    print('x1',id(x), x)
    x = 8
    print('x2',id(x), x)

a = 10
print('a1',id(a), a)
immutableObjects(a)
print('a2',id(a), a)

def mutableObjects(x):
    print('x1',id(x))
    x[2] = 20
    print('x2',id(x))

a = [10,15,18]
print('a1',id(a), a)
mutableObjects(a)
print('a2',id(a), a)M