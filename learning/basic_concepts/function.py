
def printFn(str):
    print("Hello "+ str)

printFn("Venkatraman")

def add(a,b):
    return a+b

x = add(7,8)

print(x)

def add_sub(a,b):
    return a+b, a-b

addVal, subVal = add_sub( 18, 6)
print(addVal, subVal)