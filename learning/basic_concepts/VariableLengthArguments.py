def person(name, *d):
    print(name)
    print(d)

person('Venkatraman', 36, 'Chennai')

def person(name, **d): #notice the two asterisks to handle key arguments
    print(name)
    print(d)

person(name='Venkatraman', age=36, city='Chennai')