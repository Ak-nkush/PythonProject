class Factorial :
    def __init__(self,num):
             self.num  = num
    def calculate_factorial(self) :
        factorial = 1
        for i in range(1,self.num+1) :
            factorial = factorial * i
        return factorial

x = int(input("Enter a number: "))
y = Factorial(x)
print(f"The factorial of {x} is {y.calculate_factorial()}")