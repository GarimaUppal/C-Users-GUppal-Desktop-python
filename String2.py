Stringinput= input("Enter the string: ")
Stringinput=list(Stringinput)
print(Stringinput)

for i in Stringinput:
    if Stringinput[i].isalpha():
        letters+=1
    print("is Alphabet", i)
    else:
        print("Stringinput is digit")
