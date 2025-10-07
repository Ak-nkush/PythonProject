monthNames = list(("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"))
# take the number from the user
# determine the number is between 1 to 12
# and return the corresponding number

num = int(input("Enter a number: "))
if(num>=1 and num<=12):
    print(monthNames[num-1])
else:
    print("Invalid input")

# EXIT is use to terminate the execution of the code
