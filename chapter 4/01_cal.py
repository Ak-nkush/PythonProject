class Calculator:
    def __init__(self):
        pass
    def addition(self,num1,num2):
        res = num1 + num2
        print(f"The addition of {num1} and {num2} is {res}")

    # this have a higher authority
    # called as variable argument
    def additon(self,*num):
        # n number of parameter are taken -> *num
        # this variables are treated as a list that the reason we are using loop
        #
        res = 0
        for n in num :
            res += n
        print(f"The addition of {num} is {res}")

calObj = Calculator()
calObj.addition(1,2)
calObj.additon(1,2,3,4,5)