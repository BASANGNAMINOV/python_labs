a=input("ФИО:")
b=a.split()
a1=b[0][0]
a2=b[1][0]
a3=b[2][0]
print("Инициалы:"+a1.upper()+a2.upper()+a3.upper()+".","\nДлина:",len(a)-a.count(" ")+2)