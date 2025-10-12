# with using readline() calculate calculate non blank (no of lines) in a file

class Solution :
    def __init__(self,myfile):
        self.myfile = myfile

    def calculate_lines(self) :
        filedata = self.myfile.readlines()
        lines = 0
        for i in filedata :
            if i != '\n' :
                lines += 1
        return lines

myfile = open("00_file.text","r")
x = Solution(myfile)
y = x.calculate_lines()
print(y)