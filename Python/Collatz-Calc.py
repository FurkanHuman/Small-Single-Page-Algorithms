from ast import arg
import sys

ct=0
## argList=sys.argv

inputNumber=int(input("Enter Number here: "))

print(ct,"=",int(inputNumber))


while(True):
    ct=ct+1
    if(inputNumber==1):
        break

    if(inputNumber%2==0):
        inputNumber=(inputNumber/2)

    else:
        inputNumber=(inputNumber*3)+1

    print(ct,"=",int(inputNumber))
exit()