'''password= input("Enter the password: ")
print("number of words in password: ",len(password))
length=len(password)
char=0
passwd=0
if (length > 5 and length < 13):
    print("Password length achieved")

#Passwd=list(password)
for i in password:
    if  char in ["@","#","&"]:
        i+=1
        print("Symbol used", password)


if length>=13:
    print("reduce password length")

    
for i in password:
    if i != i.isalnum():
        char+=1
        print("one character is used",i)'''
    


password=input("enter password:")
flag=0
if ("#" in password or "@" in password) and (len(password) >=6 and len(password) <=12):
    flag =1

if flag ==1:
    print("valid password")
else:
    print("invalid password")
                                             
                                             
