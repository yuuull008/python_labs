fio=input('ФИО:')
fio=fio.upper()
f,i,o=fio.split()
print(f'Инициалы: {f[0]}{i[0]}{o[0]}.')
print('Длина (символов):', len(' '.join(fio.split())))

