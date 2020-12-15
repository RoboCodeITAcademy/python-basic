# t=truck  c=car  b=bike +m=money +w=workers +t=tushum
print("######### Moyka(kunlik daromat) ##########")

t=int(input("yuk mashinalari:"))
tm=int(input("narxi(1)"))
tw=int(input("ishchilar soni:"))
twm=int(input("ishchilar ulushi(%):"))
tt=tm*t
maosh_1=((tm*t/100)*twm)
natija_1=tt-((tm*t/100)*twm)
print("ishchilar maoshi:",maosh_1)
print("sof foyda:",natija_1)

c=int(input("yengil mashinalar:"))
cm=int(input("narxi(1)"))
cw=int(input("ishchilar soni:"))
cwm=int(input("ishchilar ulushi(%):"))
ct=cm*c
maosh_2=((cm*c/100)*cwm)
natija_2=ct-((cm*c/100)*cwm)
print("ishchilar maoshi:",maosh_2)
print("sof foyda:",natija_2)

b=int(input("mototsikllar:"))
bm=int(input("narxi(1)"))
bw=int(input("ishchilar soni:"))
bwm=int(input("ishchilar ulushi(%):"))
bt=bm*b
maosh_3=((bm*b/100)*bwm)
natija_3=bt-((bm*b/100)*bwm)
print("ishchilar maoshi:",maosh_3)
print("sof foyda:",natija_3)

g=int(input("gilam:"))
gm=int(input("narxi(1)"))
gw=int(input("ishchilar soni:"))
gwm=int(input("ishchilar ulushi(%):"))
gt=gm*g
maosh_4=((gm*g/100)*gwm)
natija_4=gt-((gm*g/100)*gwm)
print("ishchilar maoshi:",maosh_4)
print("sof foyda:",natija_4)

natija=natija_1+natija_2+natija_3+natija_4
print("$$$ UMUMIY DAROMAT $$$",natija)
finish=input("hulosa:") 
print(finish)
