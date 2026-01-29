ucheck=0
echeck=0
phcheck=0
agecheck=0

username = (str(input("enter your username:")))
LENu = len(username)

email = (str(input("enter your email:")))
LENe = len(email)

phone = (str(input("enter your phone:")))
LENph = len(phone)

age=(int(input("enter your age:")))

if (username[0] != " " and username[LENu-1] != " "):
    if(username.count(" ")>=1):
        ucheck = 1
if(email.find("@")>0 and email.find(".")!=-1 and email[0].isalpha() and email.find(" ")==-1):
    echeck=1
else:
    echeck=0
if(age>=18 and age<=60):
    agecheck = 1
else:
    agecheck = 0
if(phone.isdigit()):
    if(LENph==10 and phone[0]!="0"):
        phcheck = 1
    else:
        phcheck = 0
else:
    phcheck = 0
if(ucheck and echeck and agecheck and phcheck):
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")
