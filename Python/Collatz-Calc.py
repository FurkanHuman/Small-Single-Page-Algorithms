ct = 0

inputNumber = float(input("Enter Number here: "))

print(ct, "=", inputNumber)

of = open(str(inputNumber)+".txt", "a")
of.write(str(ct)+" = "+(str(inputNumber)+'\n'))

while(True):
    ct = ct+1

    if(inputNumber == 1 or inputNumber == -1):
        break

    elif(inputNumber % 2 == 0):
        inputNumber = (inputNumber/2)

    elif(inputNumber < 0):
        inputNumber = (inputNumber*3)-1

    else:
        inputNumber = (inputNumber*3)+1

    of.write(str(ct)+" = "+(str(inputNumber)+'\n'))
    print(ct, "=", inputNumber)

of.flush()
of.close()
exit()
