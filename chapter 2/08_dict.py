# since python 3.7 dictionary is ordered

myDict = { 1 : "Apple" , 2:"Cherry",3:"Banana",4:"Peach"}

print(myDict)
print(type(myDict))
print(len(myDict)) #counts the numbers of elements in a dictionary
print("*************")

studentRecord = {'name':"ABC" , 'age' : 20 , 'contactNumbers':[123456,76546]}
print(studentRecord)

onemoreStudentRecord = studentRecord
print("looking at new dictionary: " , onemoreStudentRecord)
print(type(onemoreStudentRecord))

