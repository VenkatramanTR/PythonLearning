# for else prints the else block when the entire for loop is executed without executing the break statement
# Rule is we need to have a break statement inside the for loop

x = [1,12,14,18,21,24]

for i in x:
    if(i % 5 == 0):
        print(i)
        break
else:
    print("not divisible by 5") # no value is divisible by 5 so printing the else block of for
