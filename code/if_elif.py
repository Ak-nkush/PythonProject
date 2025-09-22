age = int (input("Enter your age : "))
# the data entered into the console is always a string soo we have too typecast it
if(age < 18 ) :
    print("You are not an adult yet")
elif(age == 18 ) :
    # print("Just an adult")
    pass
# pass keyword is used when action is not specified , there would be not a core statement , just a placeholder for a future use , line below pass will be executed
else :
    print("legally an adult!!")