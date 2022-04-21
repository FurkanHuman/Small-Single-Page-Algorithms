ct=0

inputNumber=float(input("Enter Number here: "))

print(ct,"=",inputNumber)

while(True):
    
    ct=ct+1

    if(inputNumber==1 or inputNumber==-1):
        break

    if(inputNumber%2==0):
        inputNumber=(inputNumber/2)

    else:
        inputNumber=(inputNumber*3)+1

    print(ct,"=",inputNumber)
exit()