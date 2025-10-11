# write a program to determine if a given string is a palindrome or not using combination of positive and negative indexing.Take the string from the user
class Palindrome:
    def __init__(self, str):
        self.str = str

    def checkPalindrome(self):
        a = 0
        b = len(self.str) - 1
        while a <= b:
            if self.str[a] != self.str[b]:
                print("Not a palindrome")
                return
            a = a + 1
            b = b - 1
        print("Its a palindrome")


st = input("Enter a string to check whether it is palindrome string or not: ")
x = Palindrome(st)
x.checkPalindrome()



