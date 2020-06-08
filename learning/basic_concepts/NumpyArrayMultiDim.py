from numpy import *
arr = array([[1,2,3],[4,5,6]])
print(arr)
print(arr.dtype)
print(arr.ndim) #dimension of array
print(arr.shape) #rows and columns
print(arr.size)

arr2 = arr.flatten()
print(arr2) # converts to single dimension

arr3 = arr2.reshape(3,2,1)
print(arr3)