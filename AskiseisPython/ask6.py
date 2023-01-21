import datetime
days= ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
y = int(input("Dwse Xrono:"))
m = int(input("Dwse Mina:"))
#briskw poses meres exei o minas
if (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
    x=31
elif m==2:
    #An einai disekto
    if y%4==0:
        x=29
    else:
        x=28
else:
    x=30








for i in range (1,x+1):
    tday=datetime.date(y,m,i)
    
    g=(tday.weekday())

    
    print (tday)
    print (days[tday.weekday()])
	