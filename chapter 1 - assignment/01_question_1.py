# write a program to determine if a given string is a palindrome or not using combination of positive and negative indexing.Take the string from the user

st = input("Enter a string to check whether it is  palindrome string or not :")
a = 0
b = len(st) - 1
check = True
while a < b:
    if st[a] != st[b]:
        check = False
        break
    a = a + 1
    b = b - 1

if check :
    print(f"Given String- {st},is palindrome")

else :
    print(f"Given String- {st},is not palindrome")

