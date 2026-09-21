min=int(input("Минуты:"))
hour=min//60
if min%60<10:
    newmin='0'+str(min%60)
else:
    newmin=str(min%60)
print(f"{hour}:{newmin}")


