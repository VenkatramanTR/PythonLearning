from functools import reduce

def is_even(num):
    return num%2 == 0

def makeDouble(num):
    return num*2

def add_all(num1, num2):
    return num1+num2
nums = [2,5,7,9,11,3,4,6,8,10]

#evens = list(filter(is_even,nums)) -->
evens = list(filter(lambda n: n%2==0, nums))

#doubles = list(map(makeDouble, evens))

doubles = list(map(lambda n : n*2, evens))# though filter and map looks same, we cannot use filter here, as
                                        # filter will just return the item and it will not do any opration
                                        # like doubles(multiplication by 2) on items
sum = reduce(lambda a,b : a+b, doubles)
#sum = list(map(lambda a,b : a+b, doubles))
print("even values --> ",evens)
print("double values -->",doubles)
print("final sum --> ",sum)
