myfile = open("abc.text","r")
print(myfile.read())

# repositioning the file pointer to the beginning of the file or at the any position on the file
# this can be done using seek()
# playing with the pointer in a file
myfile.seek(0)
print(myfile.read(4))

# determining the current position of the cursor in a file
# for that we are using myfile.tell()
print("Currently cursor is on which character " , myfile.tell())

# repositioning the pointer
myfile.seek(10)
print("File pointer repositioned ")
print(myfile.read(10))

# reading the file without using
print("Reading line by line without using readline() ")
myfile.seek(0)
for line in myfile:
    print(line)


