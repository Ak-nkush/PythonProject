class Occurrence :
    def __init__ (self,string,key):
        self.string = string
        self.key = key


    def count_character (self):
        count = 0
        for i in self.string :
            if i == self.key:
                count += 1
        return count

string = input("Enter String: ")
key = input("Enter the character that you have to count in a above string: ")

str = Occurrence(string,key)
print(f"The occurrence of {key} in {string} is {str.count_character()}")