def format_record(rec: tuple[str, str, float]) -> str:
    """Форматирует запись про студента. TypeError: rec не является tuple, ФИО/группа пустые, GPA не тот тип.
    ValueError: tuple имеет неверную длину, в ФИО неверное кол-во слов, GPA вне диапазона 
    """
    if not isinstance(rec,tuple):
        raise TypeError('не тот тип входных данных')
    if len(rec)!=3:
        raise ValueError('неправильная длина кортежа')
    fio, group, gpa = rec 
    fio=' '.join(fio.split())
    group=' '.join(group.split())
    if not fio:
        raise TypeError('Строка ФИО пустая')
    if not group:
        raise TypeError('Строка группы пустая')
    part=fio.split()
    if len(part)!=2 and len(part)!=3:
        raise ValueError('ФИО неверной длины')
    if not isinstance(gpa,(int,float)):
        raise TypeError('GPA не число')
    if not(0.0 <= gpa <= 5.0):
        raise ValueError('GPA вне диапазона')
    initials=''
    sn=part[0].capitalize()
    for name in part[1:]:
        initials+=name[0].upper()+'.'
    return f'{sn} {initials}, гр. {group}, GPA {gpa:.2f}'

#тест-кейсы
print('format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)) ->', format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print('format_record(("Петров Пётр", "IKBO-12", 5.0)) ->', format_record(("Петров Пётр", "IKBO-12", 5.0)))
print('format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)) ->', format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print('format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)) ->', format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
try:
    print(f'format_record(("", "BIVT-25", 4.6)) ->',format_record(("", "BIVT-25", 4.6)))
except (ValueError, TypeError) as error:
    print(f'format_record(("", "BIVT-25", 4.6)) -> {type(error).__name__}: {error}')
try:
    print(f'format_record(("Иванов Иван Иванович", "", 4.6)) ->',format_record(("Иванов Иван Иванович", "", 4.6)))
except (ValueError, TypeError) as error:
    print(f'format_record(("Иванов Иван Иванович", "", 4.6)) -> {type(error).__name__}: {error}')
try:
    print(f'format_record(("Иванов Иван Иванович", "BIVT-25", 8.00)) ->',format_record(("Иванов Иван Иванович", "BIVT-25", 8.00)))
except (ValueError, TypeError) as error:
    print(f'format_record(("Иванов Иван Иванович", "BIVT-25", 8.00)) -> {type(error).__name__}: {error}')