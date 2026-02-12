n=int(input("enter number:"))
data=[0]*n
for i in range(n):
    x=input("enter data:")
    if x.isdigit():
        data[i]=int(x)
    else:
        data[i]=x
number=[]
string=[]
for i in data:
    if type(i)==str and len(i)>0 :
        string.append(i)
    elif type(i)==int:
        number.append(i)
    else:
        pass

print("my register number is even(AP24110011704) so printing number list in reverse order:")
print("="*50)
print("list before reversing:")
print(number)
print("list after reversing:")
print(number[len(number)-1:-1*(len(number))-1:-1])
print("="*50)
print("final summary:")
print("instructor test inputs:")
print(data)
print("NUMBER LIST:",number)
print("STRING LIST:",string)
print("TOTAL NUMBERS:",len(number))
print("TOTAL STRINGS:",len(string))

