from array import *
vals = array('i', [4,5,6,7,8])
newArray = array(vals.typecode, vals)
newArray2 = array(newArray.typecode, [a*a for a in newArray])

for i in vals:
    print(i, end=", ")
print()
for i in newArray:
    print(i, end=", ")

print()
for i in newArray2:
    print(i, end=", ")