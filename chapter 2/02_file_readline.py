# open the file
myfile = open("abc.text","r")
print(myfile)
# use readline to read all the lines of the given file
fileData = myfile.readline()

while fileData :
    print(fileData)
    fileData = myfile.readline()

print("The whole file is read using readline() ")

# going to read the entire file in one go - readlines
myfile.seek(0)
#  because previously we were reading the file soo the file was at end
filedata = myfile.readlines()
print(filedata)
# here the print gives the [] (square bracket) i.e a list