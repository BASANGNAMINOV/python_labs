n = int(input("in_1: "))
ochno = 0
zaochno = 0
for i in range(n):
    surname, name, age, format = input(f"in_{i + 2}: ").split()

    if format == "True":
        ochno += 1
    else:
        zaochno += 1
print(f'out : {ochno} {zaochno}')