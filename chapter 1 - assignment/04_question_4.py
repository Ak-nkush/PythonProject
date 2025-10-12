class Reverse:
    def __init__(self,string):
        self.str = string

    def reverse_string(self):
        word = ""
        newSentence = ""
        for i in range(0,len(self.str)) :
            if self.str[i] != " " :
                word += self.str[i]
            if self.str[i]==" " or i==len(self.str) - 1  :
                newSentence = word +" "+ newSentence
                word = ""

        return newSentence

st = input("Enter the string: ")
x = Reverse(st)
print("The reversed string is : ")
print(x.reverse_string())







