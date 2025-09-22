# in python match keyword is used in place of switch keyword

day = input("Enter some day of the week : ")
match day :
    case "Monday" | "monday" | "Mon" | "MON"| "MONDAY" :
         print("Today is Monday ")
    case "Tuesday" | "Tue" | "tuesday" | "TUE" | "TUESDAY" :
         print("Today is Tuesday ")
    case "Wednesday" | "monday" | "Mon" | "MON" | "MONDAY" :
         print("Today is Wednesday ")
    case "Monday" | "monday" | "Mon" | "MON" | "MONDAY" :
         print("Today is Monday ")
    case "Monday" | "monday" | "Mon" | "MON" | "MONDAY" :
         print("Today is Monday ")
    case "Monday" | "monday" | "Mon" | "MON" | "MONDAY":
        print("Today is Monday ")
    case _:
     print("You have entered invalid input , enter the valid day")
    #  default case in python should be in the last , in java default case can be written anywhere
    # default is not always mandatory

