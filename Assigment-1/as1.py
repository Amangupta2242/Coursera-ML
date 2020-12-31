import numpy as np
import matplotlib.pyplot as pt
#Raw Input
data=[]
f=open("data.txt","rt")
a=f.read().split("\n")
for i in a:
    num=i.split(",")
    data.append([float(num[0]),float(num[1])])
#Gradient decent
m,c,learn,error,mc,cc=0,0,0.001,0,0,0
n=len(data)
tm=data[0][1]/data[0][0]
tc=0
for i in data:
    error=error+(((((m*i[0])+c)-i[1])**2)/(2*n))
mi=error
for i in range(100):
    m=tm
    c=tc
    mc,cc=0,0
    error=0
    for i in data:
        error=error+(((((m*i[0])+c)-i[1])**2)/(2*n))
    for i in data:
        mc=mc+(((m*i[0])+c)-i[1])*i[0]
    for i in data:
        cc=cc+(((m*i[0])+c)-i[1])
    tm=m-(learn*mc/n)
    tc=c-(learn*cc/n)
    print(m,"+",c,"=",error)
    if error<mi:
        mf,cf=m,c
        mi=error
for i in data:
    pt.scatter(i[0],i[1]) 
for i in range(20):
    pt.scatter(i+5,mf*(i+5)+cf,marker='*') 
pt.show() 
print("\n\n",mf,"  ",cf,"+", mi)