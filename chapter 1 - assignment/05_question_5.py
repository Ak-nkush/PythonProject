class Numbers :
    def __init__(self,num):
        self.num = num
    def calculate_armstrong(self):
        sum = 0
        n = self.num
        while n > 0 :
            sum = (sum + ((n%10)**3))
            n = n//10
        if sum == self.num :
            return True
        else :
            return False

num = int(input("Enter the number to check whether it is armstrong or not: "))
x = Numbers(num)
if x.calculate_armstrong() == True :
    print(f"{num} is armstrong Number")
else :
    print(f"{num} is not armstrong Number")
