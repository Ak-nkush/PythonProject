val = int(input("Enter the number which you want to check for a PRIME condition : "))

primeSt = False
# everytime we are using a boolean variable always assign to a False value
for i in range(2,val):
    if val % i == 0:
        break
    else :
        primeSt = True

if primeSt :
    print("The number ",val," is prime")
else :
    print("The number ",val," is not prime" )
