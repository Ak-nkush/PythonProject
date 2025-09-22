while True :
     num = int(input("Enter a number"))
     if num%2 == 0 :
         print(num,"is an even number")
         continue
    # jumping to the condition again  and checks the condition
     else :
         print(num,"is an odd number")
         break

print("Goodbye")
