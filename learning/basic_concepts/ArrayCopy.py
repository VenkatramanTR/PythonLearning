from numpy import *

arr1 = array([1,2,3,4,5])
arr2 = array([6,7,8,9,10])

arr3 = arr2.copy()
print(arr3)
print(concatenate([arr2, arr1]))

print(arr1*arr1)
print(sqrt(arr1))
print(log(arr1))
print(cos(arr1))
print(sin(arr1))
print(tan(arr1))