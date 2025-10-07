num = int(input("Enter the number to check whether it is armstrong or not: "))
sum = 0
n = num
while n > 0 :
    sum  = sum + (n%10)**3
    n = n // 10

if sum == num :
    print(f"{num} is an armstrong number")
else :
    print(f"{num} is not an armstrong number")
