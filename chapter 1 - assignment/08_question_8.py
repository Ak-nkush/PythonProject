class Solution :
    def __init__(self,string):
        self.userInput = string

    def readcontent(self):
         with open("09_blankFile.txt", "w") as myfile:
             myfile.write(self.userInput)

         with open("09_blankFile.txt", "r") as myfile1:
             filedata = myfile1.read()

         print("\nThe content of the file is: ")
         print(filedata)

userInput = input("Enter the text which will be displayed in a file: ")
x = Solution(userInput)
x.readcontent()

