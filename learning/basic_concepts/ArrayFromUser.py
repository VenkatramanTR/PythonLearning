from array import *
x = array('i',[])
vals = int(input("Enter the length of the array "))
for i in range(vals):
    val = int(input("Enter the number for array "))
    x.append(val)
print(x)

search = int(input("Enter the number to search"))
for i in x:
    if i == search:
        print("value is present in position ",x.index(i)+1)
        break;
else:
    print("value is not present")
