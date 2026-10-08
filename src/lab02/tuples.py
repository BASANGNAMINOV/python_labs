def format_record(rec: tuple[str, str, int | float]) -> str:
    if not isinstance(rec, tuple):
        raise TypeError("Аргумент должен быть кортежем")
    if len(rec) != 3:
        raise ValueError("Кортеж должен содержать ровно 3 элемента")

    fio, group, gpa = rec

    if not isinstance(fio, str) or not isinstance(group, str):
        raise TypeError("ФИО и группа должны быть строками")
    if isinstance(gpa, bool) or not isinstance(gpa, (int, float)):
        raise TypeError("GPA должен быть числом")
    if not 0 <= gpa <= 5:
        raise ValueError("GPA должен быть в диапазоне от 0 до 5")

    name_parts = fio.split()
    if 2>len(name_parts)>3: 
        raise ValueError("Укажите фамилию и имя")

    if not group.strip():
        raise ValueError("Название группы не должно быть пустым")

    surname = name_parts[0].capitalize()
    initials = "".join(f"{part[0].upper()}." for part in name_parts[1:])
    formatted_name = f"{surname} {initials}"

    return f"{formatted_name}, гр. {group.strip()}, GPA {gpa:.2f}"
print(("Иванов Иван Иванович", "BIVT-25", 4.6),"=>",format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))  
print(("Петров Петр ", "IKBO-12", 5.0),"=>",format_record(("Петров Петр ", "IKBO-12", 5.0)))  
print(("Петров Пётр Петрович", "IKBO-12" , 5.0),"=>",format_record(("Петров Пётр Петрович", "IKBO-12" , 5.0)))  
print(("  сидорова  анна  сергеевна ", "ABB-01", 3.9999),"=>",format_record(("  сидорова  анна  сергеевна ", "ABB-01", 3.9999)))  

