def fib(a):
    x,y = 0,1
    while x <= a:
        x,y = y, x+y
        print(x)
fib(4)