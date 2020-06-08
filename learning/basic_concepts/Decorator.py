#Decorators are used to modify code of a function without directly editing a function. Lets say you have a
# remote function which you dont have access and you want to slightly modify the functionality of the
# function then we use decorator functionality in those cases

def div(a,b): # remote function which you dont have access
    return a/b

def smartDiv(func):
    def inner(a,b):
        if(a<b):
            a,b = b,a
        return a/b
    return inner

div_new = smartDiv(div)
div = smartDiv(div) # you can also have the same name of the original function. This line is same as that of
                    # the previous line
print(div_new(3,12))
print(div(4,20))
