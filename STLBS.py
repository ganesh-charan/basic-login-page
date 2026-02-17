L="paturu v n s ganesh charan"
print("my name:",L)
print("L=",len(L)-L.count(" "))
PLI=(len(L)-L.count(" "))%3
print("VALUE OF PLI:",PLI)
print("given list is:")
List=[4, 18, 70, -2, 30, 55, 0]
very_light=[]
normal_load=[]
heavy_load=[]
overload=[]
invalid_entries=[]
for w in List:
      if w<0:
       invalid_entries.append(w)
      elif w<=5:
        very_light.append(w)
      elif w<=25:
        normal_load.append(w)
      elif w<=60:
        heavy_load.append(w)
      else:
       overload.append(w)


print("invalid entries list:",invalid_entries)
print("very light entries list:",very_light)
print("normal load list",normal_load)
print("heavy load list",heavy_load)
print("overload list",overload)

print("since my PLI=",PLI," as per assignment RULE A is implemented")
for i in overload:
    invalid_entries.append(i)

overload=[]
print("List after moving all overload entries to invalid entries as per PLI:")
print(invalid_entries)
print("="*15)
print("ALL ENTRIES LISTS:")
print("invalid entries list:",invalid_entries)
print("very light entries list:",very_light)
print("normal load list",normal_load)
print("heavy load list",heavy_load)
print("overload list",overload)
print("="*15)
