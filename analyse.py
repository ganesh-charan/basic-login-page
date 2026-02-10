n=int(input("enter number of students: "))
print("="*150)
lis=[]
reg_no=[]

if(n>0):
   vs = n
   ivs =0
   for i in range(n):
    m=int(input(f"enter marks of student {i+1}: "))
    lis.append(m)
    reg_no.append(i*100+i%10+100)
else:
    print("invalid number of students")
print("="*150)
for i in range(n):
     m=lis[i]
     r=reg_no[i]
     if(m>=90 and m<=100 ):
       print("reg_no",r,"->",m, "->EXCELLENT")

     elif(m>=75 and m<= 89):
       print("reg_no",r,"->",m,"->VERY GOOD")

     elif(m>=60 and m<=74):
        print("reg_no",r,"->",m,"->GOOD")

     elif(m>=40 and m<= 59):
        print("reg_no",r,"->",m,"->AVERAGE")

     elif(m>=0 and m<= 39 ):
       if(r%2==0 and 39-m<=6):
        print("reg_no",r,"->",(m+6), "->PASSED BY GRACE MARKS OF 5 ")
       else:
        ivs+=1
        vs-=1
        print("reg_no",r,"->",m,"->FAIL")
     else:
      vs-=1
      print("reg_no",r,"->",m,"->INVALID MARKS")
print("="*150)

print("VALID STUDENTS:",vs)
print("FAILED STUDENTS:",ivs)
print("="*150)