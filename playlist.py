n=int(input("enter number of songs:"))
data=[0]*n
print("="*50)
for i in range(n):
    x=int(input("enter duration of song:"))
    data[i]=int(x)
x=min(data)
if (x <= 0):
    print("Invalid duration detected")
else:
    REPEAT_INDEX = 0
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] == data[j]:
                REPEAT_INDEX += 1
    TOTAL_DURATION = sum(data)
    NUMBER_OF_SONGS = len(data)
    CATEGORY = ""
    RECOMMENDATION = ""
    if REPEAT_INDEX!=0:
        CATEGORY+="REPETATIVE"
        RECOMMENDATION+="ADD NEW SONGS"
    else:
      if(TOTAL_DURATION<300):
          CATEGORY += "TOO SHORT"
          RECOMMENDATION += "LISTEN TO MORE SONGS"
      elif(TOTAL_DURATION<=3600):
          CATEGORY += "BALENCED PLAYLIST"
          RECOMMENDATION += "GOOD LISTENING SESSION"
      elif(TOTAL_DURATION>3600):
          CATEGORY += "TOO LONG PLAYLIST"
          RECOMMENDATION += "TAKE SOME BREAKS IN YOUR LISTENING SESSION"
      else:
          CATEGORY += "IRREGULAR"
          RECOMMENDATION += "RANDOM LISTENING SESSION"
      if(NUMBER_OF_SONGS%2==0):
          CATEGORY += " EVEN PLAYLIST"

    print("=" *50 )
    print("TOTAL DURATION OF SONGS:", TOTAL_DURATION)
    print("TOTAL NUMBER OF SONGS:", NUMBER_OF_SONGS)
    print("CATEGORY:", CATEGORY)
    print("RECOMMENDATION:", RECOMMENDATION)
