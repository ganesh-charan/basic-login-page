L="paturu v n s ganesh charan"
print("value of L:",L)
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


print(invalid_entries)
print(very_light)
print(normal_load)
print(heavy_load)
print(overload)