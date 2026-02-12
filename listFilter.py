data=[10,"python","",25,"Loop",40]
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

