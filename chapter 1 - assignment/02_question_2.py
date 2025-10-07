st = input("Enter String: ")
ch = input("Enter the character that you have to count in a above string: ")

countCharacter = 0
for i in range(len(st)):
    if st[i] == ch:
       countCharacter += 1

print(f"Count of {ch} in a above string is {countCharacter}")