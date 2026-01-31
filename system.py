scheck=0
echeck=0
pcheck=0
rcheck=0
studentID = input("Enter Student ID: ")
emailID = input("Enter Email ID: ")
password=input("Enter Password: ")
referral_code=input("Enter Referral Code: ")
if(studentID.startswith("CSE-")
        and studentID[4].isdigit()
        and studentID[5].isdigit()
        and studentID[6].isdigit()
        and len(studentID)==7):
    scheck=1
if(emailID.endswith("@univ.edu")
        and'a'<=emailID[0].lower()<='z'
        and emailID.count("@")==1
        and emailID.count(".")==1
        and emailID.find(" ")==-1):
    echeck=1
if( len(password)>=8
    and 'A'<= password[0] <='Z'
    and ('0' in password or '1' in password or
        '2' in password or '3' in password or
        '4' in password or '5' in password or
        '6' in password or '7' in password or
        '8' in password or '9' in password)):
    pcheck=1
if( len(referral_code)==6
        and referral_code.startswith("REF")
        and referral_code[3].isdigit() and referral_code[4].isdigit()
        and referral_code.endswith("@") ):
    rcheck=1
if(scheck==1 and echeck==1 and rcheck==1 and pcheck==1):
    print("APPROVED")
else:
    print("s :",scheck,"e :", echeck,"r: ", rcheck,"p: ", pcheck)
    print("REJECTED")