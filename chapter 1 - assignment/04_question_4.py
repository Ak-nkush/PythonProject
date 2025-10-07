st = input("Enter the string: ")

word = ""
sentence = ""
for i in range(len(st)-1,-1,-1):
    if st[i] != " " :
        word  = st[i] + word
    elif st[i] == " " :
        sentence = sentence + " " + word
        word = ""

    if st[i] != " " and i == 0 :
        sentence = sentence + " " + word

print(sentence)



