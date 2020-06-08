
def fact(n):
    f = 1
    for i in range(n):
        f = f * (i+1)
    print(f)

#fact(5)
finalVal = 1

def facRecursive(n):
    if n==0:
        return 1
    return n * facRecursive(n-1)

print(facRecursive(5))
