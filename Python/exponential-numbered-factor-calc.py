import time

x=int(input("Enter Base: ")) #Base.
y=int(input("Enter Exponent: ")) #Exponent.

f=1 # Just equals 1

ce = x**y #Calculated exponent number

file=open(str(ce)+"#FILE_NAME.txt","a") 

print(ce)
for n in range(1,ce+1) :
 # start_time = time.time() # Measure calculation time
    f=f*n
 # start_time=(time.time() - start_time)
    print(n," ",f," ")
 # print("--- %s seconds ---" %start_time)
print(f)

file.write(str(f))
file.flush()
file.close()