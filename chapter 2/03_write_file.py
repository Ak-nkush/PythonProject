# create a file
myfile = open("StudentData.text" , "w")

addmore = True
while addmore:
    stNm = input("enter your name: ")
    myfile.write(stNm)
    myfile.write("\n")
    st = input("Enter f/F if you want to stop adding the name or else enter ENTER key ")
    if st == "f" or st == "F":
        addmore = False
print("AlL the names in a file ")

myfile = open("StudentData.text" , "r")
print("The names added to the file are given below : ")
stNms = myfile.readlines()
for stNm in stNms:
    print(stNm)
myfile.close()