import csv
crimes={}
with open("crimes.csv") as f:
    for row in list(csv.reader(f))[1:]:
        if row[2][6:10]=="2015":
            crime=row[5]
            if crime in crimes:
                crimes[crime]+=1
            else:
                crimes[crime]=1
            #print(row[2][6:10],row[5])
#for crime in crimes:
 #   if crime[2][6:10]=="2015":
  #      print(crime[2][6:10],crime[5])
m=max(crimes.values())
for key,value in crimes.items():
    if value==m:
        print(key)
