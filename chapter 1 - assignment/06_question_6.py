# built own readline() method

class Solution :
    def __init__(self, myfile):
        self.myfile = myfile

    def readLine(self):
        self.myfile.seek(0)
        for line in self.myfile:
            print(line,end="")

myfile = open("00_file.text","r")
x = Solution(myfile)
x.readLine()

